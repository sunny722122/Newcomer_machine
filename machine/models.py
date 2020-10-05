from django.db import models
from phone_field import PhoneField
from djmoney.models.fields import MoneyField

# Create your models here.
#images
class imageLibrary(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}: {self.description}"
        
#machine characteristic
class characteristic(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}:  Des:{self.description}"

#machine technical specification
class techspec(models.Model):
    name=models.CharField(max_length=40)
    param=models.CharField(max_length=60)
    def __str__(self):
        return f"{self.name}:{self.param} "

#standard equipment
class stdequipment(models.Model):
    name=models.CharField(max_length=40)
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="stdequipimage")
    descr=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.descr}"

#attachments and accessories
class attach(models.Model):
    name=models.CharField(max_length=40)
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="attachimage")
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.description}"

#machine category
class MachineCategory(models.Model):
    name=models.CharField(max_length=40)
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="mcimagelibrary")
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}: Description: {self.description}"

#datasheet or brochure
class datasheet(models.Model):
    name=models.CharField(max_length=40)
    filepath=models.FileField()
    description=models.CharField(max_length= 400)
    def __str__(self):
        return f"{self.name}: {self.description}"

#machine
class Machine(models.Model):
    maincategoryID=models.ForeignKey(MachineCategory,on_delete=models.CASCADE,related_name="machinecategory")
    name=models.CharField(max_length=40)
    price=MoneyField( max_digits=14, decimal_places=2, default_currency='CAD',null=True)
    imgid=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="mimages")
    summary=models.CharField(max_length=500)
    character=models.ManyToManyField(characteristic,blank=True,null=True,related_name="machines")
    techspec=models.ManyToManyField(techspec,blank=True,null=True,related_name="techspec")
    stdequip=models.ManyToManyField(stdequipment,blank=True,null=True,related_name="standardequipment")
    attach=models.ManyToManyField(attach,blank=True,null=True,related_name="attachment")
    descr=models.CharField(max_length=2000)
    datash=models.ForeignKey(datasheet,blank=True, null=True, on_delete=models.CASCADE,related_name="datasheet")
    def __str__(self):
        return f"{self.name}:{self.summary} Description:{self.descr}"

#customer's information
class customercontact(models.Model):
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=100)
    addr=models.CharField(max_length=100)
    postcode=models.CharField(max_length=7)
    city=models.CharField(max_length=20)
    area=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    telinfo=models.CharField(max_length=11)
    mobilinfo=models.CharField(max_length=11)
    subject=models.CharField(max_length=200,default="request")
    message=models.CharField(max_length=500)
    def __str__(self):
        return f"{self.name}:{self.message}"

#company contact
class companycontact(models.Model):
    companyname=models.CharField(max_length=40)
    addr=models.CharField(max_length=40)
    telinfo=PhoneField(blank=True, help_text='Contact phone number')
    faxinfo=PhoneField(blank=True, help_text='Contact fax number')
    email=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.companyname}:{self.email}"
