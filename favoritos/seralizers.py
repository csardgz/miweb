from rest_framework import serializers
from .models import Favoritos

class FavoritosSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ('id','nombre','apellido','url')



