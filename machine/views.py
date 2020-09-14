from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request,"machines/index.html",{
        "machinecategory":MachineCategory.objects.all(),
        "machines":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })

def category(request,category):
    categories=MachineCategory.objects.get(name=category)
    machines=Machine.objects.get(maincategoryID=categories)
    return render(request,"machines/category.html",{
        "categories":categories,
        "machines":machines,
        "machinecategory":MachineCategory.objects.all(),
        "machineall":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })