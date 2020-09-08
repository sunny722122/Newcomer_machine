from django.contrib import admin
from .models import *

# Register your models here.
# machinecategory
class MachineCategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","machineID","imgID","description")

class MachineAdmin(admin.ModelAdmin):
    list_display=("id","maincategoryID","imgId","summary","character","techspec","stdequip","attach","descr","datash")

class ChateristicAdmin(admin.ModelAdmin):
    list_display=("id","name","machineID","description")

admin.site.register(MachineCategory,MachineCategoryAdmin)
admin.site.register(Machine)
admin.site.register(characteristic)
admin.site.register(techspec)
admin.site.register(stdequipment)
admin.site.register(attach)
admin.site.register(datasheet)
admin.site.register(imageLibrary)
admin.site.register(customercontact)
admin.site.register(companycontact)