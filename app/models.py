from email.mime import image
from itertools import product
from pydoc import describe
from typing import Tuple
from unicodedata import category
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,  null=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True,  null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    
class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='item')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,  null=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    
    
    def __str__(self):
        return self.name
    
   
   
class Description(models.Model):
    description = models.TextField(blank=True,  null=True)
    
    class Meta:
        verbose_name_plural = "Description"
        
        
    def __str__(self):
        return self.description
    
    
def get_product_by_category(category: str) -> Tuple[Category]:
    return Category.objects.filter(category__name=category).all()  
    
    
    
    
    
    
    
    
    