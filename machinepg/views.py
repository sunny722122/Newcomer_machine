from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request,"machines/index.html",{
        "machinecategory":MachineCategory.objects.all(),
        "machines":Mahine.objects.all(),
        "images": imageLibrary.objects.all(),
        "contact":companycontact.objects.all(),
    })