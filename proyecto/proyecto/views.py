
from django.template import Template, context
from django.shortcuts import render
from django.http import HttpResponse



def inicio(request):
    return render(request,'inicio.html',{
        #context
    })

def nosotros(request):
    return render(request,'nosotros.html',{
        #context
    })

def contacto(request):
    return render(request,'contacto.html',{
        #context
    })

def catalogo(request):
    return render(request,'catalogo.html',{
        #context
    })

def login(request):
    return render(request,'login.html',{
        #context
    })

def usuario(request):
    return render(request,'usuario.html',{
        #context
    })

def inicioU(request):
    return render(request,'inicious.html',{
        #context
    })

def contactoU(request):
    return render(request,'contactous.html',{
        #context
    })

def catalogoU(request):
    return render(request,'catalogous.html',{
        #context
    })

def nosotrosU(request):
    return render(request,'nosotrosus.html',{
        #context
    })