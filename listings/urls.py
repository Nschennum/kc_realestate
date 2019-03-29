from django.urls import path

from . import views

#path, method, name '/' pertains to /listings and index is specific to listings

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]