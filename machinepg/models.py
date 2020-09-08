from django.db import models

# Create your models here.
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


class characteristic(models.Model):
    name=models.CharField(max_length=40)
    
    description=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}:  Des:{self.description}"

class techspec(models.Model):
    name=models.CharField(max_length=40)
    
    param=models.CharField(max_length=60)
    def __str__(self):
        return f"{self.name}:{self.param} "

class stdequipment(models.Model):
    name=models.CharField(max_length=40)
    
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="imagelibrary")
    descr=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.descr}"

class attach(models.Model):
    name=models.CharField(max_length=40)
    #machineID=models.IntegerField(max_length=500)
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="imagelibrary")
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:{self.description}"



class MachineCategory(models.Model):
    name=models.CharField(max_length=40)
    categoryID=models.IntegerField()
    #machineID=models.ManyToManyField(Machine,blank=True,related_name="passengers")
    imgID=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="imagelibrary")
    description=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}:Category:{self.categoryID} Description: {self.description}"

class datasheet(models.Model):
    name=models.CharField(max_length=40)
    #cateID=models.ForeignKey(MachineCategory,on_delete=models.CASCADE,related_name="machinecategory")
    #machineID=models.ForeignKey(Machine,on_delete=models.CASCADE,related_name="machine")
    filepath=models.FileField()
    description=models.CharField(max_length= 400)
    def __str__(self):
        return f"{self.name}: {self.description}"

class Machine(models.Model):
    maincategoryID=models.ForeignKey(MachineCategory,on_delete=models.CASCADE,related_name="machinecategory")
    name=models.CharField(max_length=40)
    imgId=models.ForeignKey(imageLibrary,on_delete=models.CASCADE,related_name="imagelibrary")
    summary=models.CharField(max_length=500)
    character=models.ForeignKey(characteristic,on_delete=models.CASCADE,related_name="characteristic")
    techspec=models.ForeignKey(techspec,on_delete=models.CASCADE,related_name="techspec")
    stdequip=models.ForeignKey(stdequipment,on_delete=models.CASCADE,related_name="standardequipment")
    attach=models.ForeignKey(attach,on_delete=models.CASCADE,related_name="attachment")
    descr=models.CharField(max_length=500)
    datash=models.ForeignKey(datasheet,on_delete=models.CASCADE,related_name="datasheet")
    def __str__(self):
        return f"{self.name}:{self.summary} Description:{self.descr}"

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
