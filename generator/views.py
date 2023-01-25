from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):

    #tengo mi lista de caracteres para la contraseña
    characters = list('abcdefghijqlmnñopqrstuvwxyz')
    generated_password = ''

    #obtengo de la URL el numero de caracteres
    lenght = int(request.GET.get('lenght'))

    #obtengo si esta actuava la mayus o no, y extiendo la lista con esos caracteres
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    #obtengo si esta activa la opcion caracteres especiales, si es asi le añado esos caracteres a mi lista
    if request.GET.get('special'):
        characters.extend(list('_-*+$%&@'))

    #obtengo si esta activa la opcion de numeros, si es asi le añado esos numeros a la lista
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    #recorro la lista de letras y guardo de manera aleatoria los caracteres
    for char in range(lenght):
        generated_password += random.choice(characters)

    #muestro la contraseña generada
    return render(request, 'password.html', {'password': generated_password})