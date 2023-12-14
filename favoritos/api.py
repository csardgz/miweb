from .models import Favoritos
from rest_framework import viewsets, permissions
from .seralizers import FavoritosSeralizer

class FavoritosViewSet(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FavoritosSeralizer