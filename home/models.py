from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    message=models.TextField(default=False)
    
    def __str__(self):
        return self.name


class Author(models.Model):
   
    authorname=models.CharField(max_length=100)
    authorbio=models.CharField(max_length=10000)
    authorinterest1=models.CharField(max_length=1000)
    authorinterest2=models.CharField(max_length=1000)
    authorinterest3=models.CharField(max_length=1000)
    authorimagelink=models.CharField(max_length=10000000000)
    


