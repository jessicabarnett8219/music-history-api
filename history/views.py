from history.models import Artist, Song, Album
from rest_framework import viewsets
from history.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'artists': reverse('artists', request=request, format=format),
        'albums': reverse('albums', request=request, format=format),
        'songs': reverse('songs', request=request, format=format)
    })


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

