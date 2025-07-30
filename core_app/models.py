from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    iamge = models.ImageField(upload_to="category_img", blank=True, null= True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    decription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()
    image = models.ImageField(upload_to="product_img", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products_in_this_category")


    def __str__(self):
        return self.name
    
