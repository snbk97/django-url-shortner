from django.db import models
from django.conf import settings
from django.contrib import admin
from django.urls import reverse
from . import utils


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'date', 'shortcode', 'active', 'clicks',)


class LinkModelManager(models.Manager):
    def refresh_code(self):
        qs = Link.objects.filter(pk__gte=1)
        for q in qs:
            q.shortcode = None     
            q.save()
            print(q.shortcode)


class Link(models.Model):
    class Meta:
        verbose_name_plural = "Links"
        ordering = ('-date',)

    url = models.URLField('URL', unique=False, blank=False, null=False)
    shortcode = models.CharField('ShortCode', max_length=10, unique=True, blank=True, null=False)
    date = models.DateField('Date', auto_now_add=True)
    active = models.BooleanField('Active', default=True)
    clicks = models.IntegerField('Clicks', default=0)

    objects = LinkModelManager()

    def get_short_url(self):
        return settings.SITE_URL + self.shortcode

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = utils.code_gen(self)
        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
