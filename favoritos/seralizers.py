from rest_framework import serializers
from .models import Favoritos

class FavoritosSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ['nombre','apellido','url']



