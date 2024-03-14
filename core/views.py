from django.shortcuts import render, redirect
from .models import Dogovor



def home(request):

    return render(request, 'core/home.html')

def d_admin(request):

    if request.method == 'POST':
        text = request.POST.get('content_input') 
        dog = Dogovor.objects.create(text=text) 
        return render(request, 'core/admin_success.html', {'dog_id': dog.id, 'dog':dog})  
    
    return render(request, 'core/d_admin.html')


def d_cilent(request, dog_id):
    dog = Dogovor.objects.get(pk=dog_id)

    if request.method == 'POST':
        fio_cilent = request.POST.get('fio_cilent')
        if fio_cilent != '':
            dog.fio_cilent = fio_cilent
            dog.save()
            dogg = Dogovor.objects.get(pk=dog_id)
            return render(request, 'core/cilent_success.html', {'fio_cilent':fio_cilent,'dog': dogg})
        

    context = {
        'dog': dog
    }
    return render(request, 'core/d_cilent.html', context)


def list_dog(request):

    list_dog = Dogovor.objects.all()[::-1]
    return render(request, 'core/list_dog.html', {'dogs':list_dog})


def detail(request, dog_id):
    dog= Dogovor.objects.get(pk=dog_id)

    return render(request, 'core/detail.html', {'dog': dog})