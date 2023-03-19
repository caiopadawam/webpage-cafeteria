from django.shortcuts import render, redirect
from .models import Cafe, Testemunho
from .forms import ContatenosForm


def index(request):
    cafes = Cafe.objects.all()
    testemunhos = Testemunho.objects.order_by('-data_criacao')[:3]

    if request.method == 'POST':
        contatenos_form = ContatenosForm(request.POST)
        if contatenos_form.is_valid():
            contatenos_form.save()         
            form = ContatenosForm()
            return redirect('index')
    else:
        contatenos_form = ContatenosForm()
    context = {
        'cafes': cafes, 
        'testemunhos': testemunhos, 
        'contatenos_form': contatenos_form,
    }
    return render(request, 'core/index.html', context)


def catalogo_cafe(request):
    cafes = Cafe.objects.all()
    context = {
        'cafes': cafes,
    }
    return render(request, 'core/gallery.html', context)