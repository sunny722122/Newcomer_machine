from django.contrib import admin
from .models import *

# Register your models here.
# machinecategory
class MachineCategoryAdmin(admin.ModelAdmin):
    list_display={"id","name","categoryID","machineID","imgID","description"}

class MachineAdmin(admin.ModelAdmin):
    list_display={"id","maincategoryID","imgId","summary","character","techspec","stdequip","attach","descr","datash"}

class ChateristicAdmin(admin.ModelAdmin):
    list_display={"id","name","machineID","description"}

admin.site.Register(MachineCategory,MachineCategoryAdmin)
admin.site.Register(Mahine)
admin.site.Register(characteristic)
admin.site.Register(techspec)
admin.site.Register(stdequipment)
admin.site.Register(attach)
admin.site.Register(stdequipment)
admin.site.Register(datasheet)
admin.site.Register(imageLibrary)
admin.site.Register(customercontact)
admin.site.Register(companycontact)