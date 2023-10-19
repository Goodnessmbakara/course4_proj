from django.urls import path

from .views import SearchView, DetailView


urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('detail/<str:imdb_id>/', DetailView.as_view(), name='detail'),]
