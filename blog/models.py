from django.db import models

# Create your models here.

class Post(models.Model):
    Sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=1000)
    author=models.CharField(max_length=100)
    content=models.TextField(max_length=20000)
    date_posted=models.DateTimeField()
    slug=models.CharField(max_length=300)
    also_read=models.CharField(max_length=1000)
    also_read_link=models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ' BY ' + self.author
    