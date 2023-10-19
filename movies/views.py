from django.shortcuts import render
from rest_framework import generics,status

from rest_framework.response import Response

from .models import Movie
from . serializers import MovieSerializer

from .omdb_integration import fill_movie_details, search_and_save
# Create your views here.

class SearchView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            search_and_save(query)
            return Movie.objects.filter(title__icontains=query)
        return Movie.objects.none()


class DetailView(generics.RetrieveAPIView):
    lookup_field = 'imdb_id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        fill_movie_details(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

