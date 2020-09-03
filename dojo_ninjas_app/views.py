from .models import Dojos, Ninjas
from django.shortcuts import render, redirect


def index(request):
    context = {
        'all_ninjas': Ninjas.objects.all(),
        'all_dojos': Dojos.objects.all()
    }
    return render(request, 'index.html', context)


def add_dojo(request):
    print(request.POST)
    # add a supplier to the DB
    new_dojo = Dojos.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')


def add_ninja(request):
    print(request.POST)
    # How do I get the supplier object with just the id??
    dojos_id = request.POST['dojo']
    user_instance = Dojos.objects.get(id=dojos_id)
    # add item to DB
    Ninjas.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        user_ninja=user_instance
    )

    return redirect('/')
