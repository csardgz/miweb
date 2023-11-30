from django import forms
from favoritos.models import Favoritos

class FavoritoForm(forms.Form):           #formulario/// podemos buscar info en "formularios Django"
    nombre = forms.CharField()
    apellido = forms.CharField()
    url = forms.URLField()                 #
    pass

class FavoritoModelForm(forms.ModelForm):      #
    class Meta:
        model = Favoritos
        fields = ["nombre","apellido","url"]
    pass