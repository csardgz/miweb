from django.urls import path
from favoritos.views import *


app_name = 'favoritos'

urlpatterns = [
    path('lista', lista_favoritos,name='lista'),
    path('crear',crear_favoritos,name='crear'),
    path('borrar/<int:pk>', borrar_favoritos, name='borrar'),
    #path('borrar/<int:pk>', borrar_favoritos)    #estamos diciendo que "pk" va a ser int, si no se hace esto: lo tomará como string
    path('detalle/<int:pk>',detalle_favoritos, name='detalle'),
    path('actualizar/<int:pk>',actualizar_favorito, name='actualizar')
]