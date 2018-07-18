from django.urls import path
from . import views

app_name = "shortURL"
urlpatterns = [
    path('', views.index, name='index'),
    # path('shortcode', views.shortcode, name='scode'),
    path('<shortcode>', views.redir, name ='redir'),
]