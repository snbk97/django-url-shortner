from django.contrib import admin
from .models import Link, LinkAdmin


admin.site.register(Link, LinkAdmin)
