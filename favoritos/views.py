from django.shortcuts import render, redirect
from .models import Favoritos
from .forms import FavoritoForm, FavoritoModelForm
from django.urls import reverse

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')


def lista_favoritos(request):
    
    favortos_lista= Favoritos.objects.all()     #estoy viendo en Favoritos (la lista sql) los objetos en la lista
    context = {'favoritos_lista' : favortos_lista }
    
    for fav in favortos_lista:
        print("nombre: " + fav.nombre + "\nApellido: " + fav.apellido + "\nURL: " + fav.url + "\n")


    return render(request, 'favoritos/listas.html', context)

def crear_favoritos(request):
    
    form = FavoritoForm()           #el motor de Django tiene algo llamado contexto. que es lo que podemos mandar desde las VISTA a la plantilla html
                                    #Y este contexto es un diccionario

    if request.method == "POST":
       
        form = FavoritoModelForm(request.POST) #request.POST es datos vinculantes al formulario
        context= {'form':form}
        #nombre=request.POST['nombre']
        #url=request.POST['url']
        

        if form.is_valid():                 #para obtener los datos limpios
            ##cleaned_data{} es donde podremos encontrar todos los datos del formulario validado
            #nombre = form.cleaned_data['nombre']
            #url = form.cleaned_data['url']
            #Favoritos.objects.create(nombre=nombre, url=url)     #ORM transformando de python a sql

            form.save()
        else:
            print(form.errors)
    context= {'form':form , 'titulo' : 'Agregar'}
        # fav = Favoritos()                                
        # fav.nombre = nombre
        # fav.url = url
        # fav.save()      #guardamos, crea el codigo sql y la manda a la base de datos


        

    return render(request, 'favoritos/crear.html',context)

def borrar_favoritos(request,pk):
    Favoritos.objects.get(pk=pk).delete()

    return redirect('favoritos:lista')
    #return redirect(reverse('favoritos:borrar',kwargs={'pk':pk}))

def detalle_favoritos(request,pk):
    favorito = Favoritos.objects.get(pk=pk)
    return render(request, 'favoritos/detalle.html', context={'object':favorito})

def actualizar_favorito(request,pk):
    favorito = Favoritos.objects.get(pk=pk)
    
    form =FavoritoModelForm(instance=favorito)

    if request.method == 'POST':
        
        form = FavoritoModelForm(request.POST, instance=favorito)

        if form.is_valid():
            form.save()
        else:
            print(form.errrors)
    context = {'form':form , 'titulo' : 'Actualizar'}

    return render(request, 'favoritos/crear.html', context)

