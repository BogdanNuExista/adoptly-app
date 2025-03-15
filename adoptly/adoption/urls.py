from django.urls import path
from .views import home, animal_list, add_animal, adopt_animal, edit_animal, delete_animal, detect_dog_breed
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

urlpatterns = [
    path('', home, name='home'),
    path('animals/', animal_list, name='animal_list'),
    path('add/', add_animal, name='add_animal'),
    path('adopt/<int:animal_id>/', adopt_animal, name='adopt_animal'),
    path('edit/<int:animal_id>/', edit_animal, name='edit_animal'),
    path('delete/<int:animal_id>/', delete_animal, name='delete_animal'),
    path('detect-breed/', detect_dog_breed, name='detect_dog_breed'),
]

router = DefaultRouter()
router.register(r'api/animals', AnimalViewSet)

urlpatterns += router.urls