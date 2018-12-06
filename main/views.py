from django.shortcuts import render
from rest_framework import viewsets
from .models import Song, Artist
from .serializers import ArtistSerializer, SongSerializer

# Create your views here.



class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer