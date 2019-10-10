from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_celebs" : Celebrity.objects.all()
    }
    return render(request, "celebrities/index.html", context)

def new(request):
    Celebrity.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        age=request.POST['age'],
        income=request.POST['income'],
        industry=request.POST['industry']).save()
    return redirect("/")