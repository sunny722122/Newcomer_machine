from django.urls import path

from . import views

urlpatterns=[
        path("",views.index,name="index"),
        path("<str:category>",views.category, name="category"),
        path("<str:machinename>/singlemachine",views.singlemachine,name="singlemachine"),
        path("<str:machinename>/<str:filepath>", views.download_file,name="datasheet"),
        path("about/",views.about,name="about"),
        path("contact/",views.contact,name="contact"),
        path("thanks/",views.thanks,name="thanks"),
]

