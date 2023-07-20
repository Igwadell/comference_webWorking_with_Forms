from django.shortcuts import render
from .models import Speaker


def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})


def speaker_details(request, name):
    speaker = Speaker.objects.get(name=name)
    return render(request, 'speakers/speaker_details.html', {'speaker': speaker})

# Add more views for other queries related to speakers
