from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Formerdata(models.Model):
    fid=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    aadharno=models.IntegerField()
    mobilenumber=models.IntegerField()
    gender=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)


class District(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Taluk(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Hobali(models.Model):
    taluk = models.ForeignKey(Taluk, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Village(models.Model):
    hobali = models.ForeignKey(Hobali, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Surveynumber(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name    
    
class HissaNO(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    surveyno = models.ForeignKey(Surveynumber, on_delete=models.CASCADE, null=True)
    hissano = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.hissano
    
class Peroid(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    surveyno = models.ForeignKey(Surveynumber, on_delete=models.CASCADE, null=True)
    hissano = models.ForeignKey(HissaNO, on_delete=models.CASCADE, null=True)
    period = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.period
    
class Owner(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    surveyno = models.ForeignKey(Surveynumber, on_delete=models.CASCADE, null=True)
    hissano = models.ForeignKey(HissaNO, on_delete=models.CASCADE, null=True)
    ownername = models.CharField(max_length=100,blank=True,null=True)
    extent = models.CharField(max_length=100,blank=True,null=True)
    khata = models.CharField(max_length=100,blank=True,null=True)
    cropname = models.CharField(max_length=100,blank=True,null=True)
    cropstage = models.CharField(max_length=100,blank=True,null=True)
    irrigationsource = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.ownername
