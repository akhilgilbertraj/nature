from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Faceone

# create your views here.
def home(request):
    obj=Place.objects.all()
    objone=Faceone.objects.all()
    return render(request, "index.html",{'result':obj,'resut1':objone})

