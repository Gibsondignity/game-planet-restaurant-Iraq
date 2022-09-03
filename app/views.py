from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    
    description = Description.objects.all().last()
    menus = Menu.objects.all()

    print(description)
    
    context = {"description": description, "menus": menus}
    return render(request, 'app/home.html', context)


def menu(request, name):
    menu = Menu.objects.get(name=name)
    categories = Category.objects.filter(menu=menu.id)
    context = {"menu": menu, "categories": categories}
    
    return render(request, 'app/menu.html', context)


def items(request, name):
    
    category = Category.objects.get(name=name)
    
    items = Items.objects.filter(category=category.id)
    
    context = {"category":category, "items":items, "category_name":category.menu}
    
    return render(request, 'app/items.html', context)