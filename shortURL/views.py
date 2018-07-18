from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LinkForm
from .models import Link


def index(request):
    form = LinkForm(request.POST)
    if request.POST:
        if form.is_valid():
            m_url = form.cleaned_data['url']
            ob, created = Link.objects.get_or_create(url=m_url)
            return render(request, 'shortURL/short.html', {'object': ob})
    else:
        form = LinkForm()
    return render(request, 'shortURL/index.html', {'form': form})


def redir(self, shortcode):
    qs = get_object_or_404(Link, shortcode=shortcode)
    long_url = qs.url

    qs.clicks += 1  # Count clicks
    qs.save()

    return redirect(long_url)
