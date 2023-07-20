from django.urls import path
from .views import speaker_list, speaker_details

urlpatterns = [
    path('', speaker_list, name='speaker_list'),
    path('<str:name>/', speaker_details, name='speaker_details'),
]  