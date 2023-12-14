from rest_framework import routers
from .api import FavoritosViewSet

router = routers.DefaultRouter()    #esta linea de DRF crea las url de los CRUD 
router.register('api/favoritos',FavoritosViewSet, 'favoritosrf')

urlpatterns = router.urls
