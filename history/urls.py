from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from history import views

router = DefaultRouter()
router.register('artists', views.ArtistViewSet)
router.register('albums', views.AlbumViewSet)
router.register('songs', views.SongViewSet)

urlpatterns = [
  path('', include(router.urls))
]
