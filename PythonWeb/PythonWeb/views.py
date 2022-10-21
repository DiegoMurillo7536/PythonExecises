from django.shortcuts import render 

def index(request):
    return render (request,'index.html', {
        'nombre':"Diego Murillo",
        'edad':18
    })

def contact(request):
    return render (request,'contact.html', {
    })