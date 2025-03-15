from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm, DogBreedForm
from rest_framework import viewsets
from .serializers import AnimalSerializer
from .utils.breed_detection import BreedDetector
from django.http import JsonResponse

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

from django.http import JsonResponse

def detect_dog_breed(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        form = DogBreedForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            detector = BreedDetector()
            breed = detector.detect_breed(image)  # Pass the uploaded image to the detector
            return JsonResponse({'breed': breed})  # Return the breed as JSON
        else:
            return JsonResponse({'error': 'Invalid form submission'}, status=400)
    else:
        form = DogBreedForm()
        return render(request, 'adoption/detect_breed.html', {'form': form})