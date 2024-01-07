from django.db import models

# Create your models here.
class Country(models.Model):
    Cno=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
    
class Capital(models.Model):
    Cno=models.OneToOneField(Country,on_delete=models.CASCADE)
    cap_no=models.IntegerField(primary_key=True)
    capname=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.capname
