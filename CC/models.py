from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0,'Draft'),(1,'Publish to Home'),(2,"Publish to Male wears"),
        (3,"Publish to Female wears"),(4,'Publish to T-Shirts'),
        (5,'Publish to Joggers'),(6,'Publish to Trousers'),
        (7,'Publish to Gowns'),(8,'Publish to Hoods'),
        (9,'Publish to Vintages'),(10,'Publish to foot wears'),(11,'Publish to Special offers'))

class CrownsPost(models.Model):
    BrandName=models.CharField(max_length=200, null=True)
    Slug=models.SlugField(max_length=500,unique=True,)
    Author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Crowns')
    Updated_on=models.DateTimeField(auto_now=True)
    Description=models.TextField(blank=False)
    Created_on=models.DateTimeField(auto_now_add=True)
    Status=models.IntegerField(choices=STATUS, default=0)
    Price=models.CharField(blank=True, max_length=20)
    Pic1=models.ImageField(blank=False)
    Pic2=models.ImageField(blank=False)
    Pic3=models.ImageField(blank=False)

    class Meta():
        ordering=['-Created_on']

    def __str__(self):
        return self.BrandName