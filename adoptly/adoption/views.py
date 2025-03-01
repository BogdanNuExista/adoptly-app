from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm
from rest_framework import viewsets
from .serializers import AnimalSerializer

def home(request):
    return render(request, 'adoption/home.html')

def animal_list(request):
    animals = Animal.objects.filter(is_adopted=False)
    return render(request, 'adoption/animal_list.html', {'animals': animals})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'adoption/add_animal.html', {'form': form})

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def adopt_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    
    if request.method == "POST":
        animal.is_adopted = True
        animal.save()
        return redirect('animal_list')

    return render(request, 'adoption/adopt_animal.html', {'animal': animal})

def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'adoption/edit_animal.html', {'form': form, 'animal': animal})

def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        animal.delete()
        return redirect('animal_list')

    return render(request, 'adoption/delete_animal.html', {'animal': animal})
