from history.models import Artist, Song, Album
from rest_framework import viewsets
from history.serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.AlbumViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.SongViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

