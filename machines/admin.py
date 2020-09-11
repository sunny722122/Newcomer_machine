from django.contrib import admin
from .models import *

# Register your models here.
# machinecategory
class MachineCategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","description")

class MachineAdmin(admin.ModelAdmin):
    list_display=("id","maincategoryID","name","imgid","summary","descr","datash")

class ChateristicAdmin(admin.ModelAdmin):
    list_display=("id","name","description")

class ImageAdmin(admin.ModelAdmin):
    list_display=("id","image","descr","height","width","description")

admin.site.register(MachineCategory,MachineCategoryAdmin)
admin.site.register(Machine,MachineAdmin)
admin.site.register(characteristic,ChateristicAdmin)
admin.site.register(techspec)
admin.site.register(stdequipment)
admin.site.register(attach)
admin.site.register(datasheet)
admin.site.register(imageLibrary,ImageAdmin)
admin.site.register(customercontact)
admin.site.register(companycontact)