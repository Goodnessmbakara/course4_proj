from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'runtime_minutes', 'imdb_id', 'genres', 'plot', 'is_full_record']
