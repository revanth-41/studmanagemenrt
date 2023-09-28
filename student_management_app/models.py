from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=6)
    phoneNumber=models.BigIntegerField(max_length=10)
    Qualification = models.CharField(max_length=20)
    Address = models.TextField(max_length=120)
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',default="c:/Users/ssadula/Pictures/p1.png")

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)