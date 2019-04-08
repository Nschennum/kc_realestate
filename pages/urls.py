from django.urls import path

from . import views
#path, method, name
urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about')
]