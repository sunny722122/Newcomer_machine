from django.db import models

# Create your models here.
class MachineCategory(models.Model):
    name=models.CharField(max_length=40)
    categoryID=models.IntegerField()
    machineID=models.IntegerField()
    imgID=models.IntegerField()
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:Category:{self.categoryID} Machine:{self.machineID} Description: {self.description}"

class Mahine(models.Model):
    maincategoryID=models.IntegerField()
    imgId=models.IntegerField()
    summary=models.CharField(max_length=500)
    character=models.IntegerField()
    techspec=models.IntegerField()
    stdequip=models.IntegerField()
    attach=models.IntegerField()
    descr=models.CharField(max_length=500)
    datash=models.IntegerField()
    def __str__(self):
        return f"{self.maincategoryID}:{self.summary} Description:{self.descr}"

class characteristic(models.Model):
    name=models.CharField(max_length=40)
    machineID=models.IntegerField()
    description=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}: Category: {self.machineID} Des:{self.description}"

class techspec(models.Model):
    name=models.CharField(max_length=40)
    machineid=models.IntegerField()
    param=models.CharField(max_length=60)
    def __str__(self):
        return f"{self.name}:{self.param} for machine {self.machineid}"

class stdequipment(models.Model):
    name=models.CharField(max_length=40)
    machineID=models.IntegerField(max_length=500)
    imgID=models.IntegerField()
    descr=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.descr}"

class attach(models.Model):
    name=models.CharField(max_length=40)
    machineID=models.IntegerField(max_length=500)
    imgID=models.IntegerField()
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.description}"

class datasheet(models.Model):
    name=models.CharField(max_length=40)
    cateID=models.IntegerField()
    machineID=models.IntegerField()
    filepath=models.FileField()
    description=models.CharField(max_length= 400)
    def __str__(self):
        return f"{self.name}: {self.description}"

class imageLibrary(models.Model):
    name=models.CharField(max_length=40)
    itemID=models.IntegerField()
    fpath=models.ImageField()
    descr=models.CharField(max_length=400)
    height=models.IntegerField()
    width=models.IntegerField()
    description=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}: {self.description}"

class customercontact(models.Model):
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=100)
    addr=models.CharField(max_length=100)
    postcode=models.CharField(max_length=7)
    city=models.CharField(max_length=20)
    area=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    telinfo=models.CharField(max_length=11)
    mobilinfo=models.CharField(max_length=11)
    message=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.message}"

class companycontact(models.Model):
    companyname=models.CharField(max_length=40)
    addr=models.CharField(max_length=40)
    telinfo=models.CharField(max_length=11)
    faxinfo=models.CharField(max_length=11)
    email=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.companyname}:{self.email}"
