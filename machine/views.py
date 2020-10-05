from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import mimetypes

from .models import *
from .queryform import QueryForm
from django.core.mail import send_mail

# Create your views here.
#main page
def index(request):
    return render(request,"machine/index.html",{
        "home_page":"active",
        "product_menu":"PRODUCT",
        "machinecategory":MachineCategory.objects.all(),
        "machineall":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })

#machine category
def category(request,category):
    categories=MachineCategory.objects.get(name=category)
    machines=Machine.objects.filter(maincategoryID=categories)
    return render(request,"machine/category.html",{
        "product_page":"active",
        "categories":categories,
        "machines":machines,
        "product_menu":"PRODUCT",
        "machinecategory":MachineCategory.objects.all(),
        "machineall":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })

#single machine
def singlemachine(request,machinename):
    machine=Machine.objects.get(name=machinename)
    return render(request,"machine/singlemachine.html",{
        "product_page":"active",
        "product_menu":"PRODUCT",
        "machine":machine,
        "datasheeticon": imageLibrary.objects.get(name="datasheeticon"),
        "characts":machine.character.all(),
        "machinecategory":MachineCategory.objects.all(),
        "machineall":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })

#download datasheet or brochure
def download_file(request,machinename,filepath):   
    filename = "downloaded_file_name.extension"
    fl = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

#about page
def about(request):
    return render(request,"machine/about.html",{
        "about_page":"active",
        "product_menu":"PRODUCT",
        "machinecategory":MachineCategory.objects.all(),
        "machineall":Machine.objects.all(),
        "images": imageLibrary.objects.all(),
        "logo":imageLibrary.objects.get(name="logo"),
        "contact":companycontact.objects.last(),
    })

#contact page
def contact(request):
    if request.method=='POST':
        form=QueryForm(request.POST)
        if form.is_valid():
            your_name=form.cleaned_data['your_name']
            subject=form.cleaned_data['subject']
            from_email=form.cleaned_data['your_email']
            message=form.cleaned_data['message']
            customer=customercontact()
            customer.name=your_name
            customer.email=from_email
            customer.subject=subject
            customer.message=message
            customer.save()
            try:
                send_mail(subject,message,from_email,['admin@example.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form=QueryForm()
        return render(request,"machine/contact.html",{
            "contact_page":"active",
            "form":form,
            "product_menu":"PRODUCT",
            "machinecategory":MachineCategory.objects.all(),
            "machineall":Machine.objects.all(),
            "images": imageLibrary.objects.all(),
            "logo":imageLibrary.objects.get(name="logo"),
            "contact":companycontact.objects.last(),
        })

#after query, show thanks
def thanks(request):
    return render(request,"machine/thanks.html",{
            "contact_page":"active",
            "product_menu":"PRODUCT",
            "machinecategory":MachineCategory.objects.all(),
            "machineall":Machine.objects.all(),
            "images": imageLibrary.objects.all(),
            "logo":imageLibrary.objects.get(name="logo"),
            "contact":companycontact.objects.last(),
        })