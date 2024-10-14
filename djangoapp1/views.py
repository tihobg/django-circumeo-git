from django.shortcuts import render
from djangoapp1.models import Patients
from django.http import HttpResponse


def index(request):
    context = {}
    score1 = Patients.objects.all()
    context['score1'] = score1
    context['title'] = 'Home'
    return render(request, 'index.html', context)


def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)

# Create your views here.
