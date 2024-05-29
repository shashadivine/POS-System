from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def openpos(request):
   return render (request, 'posapp/openpos.html')

def item_display(request):
   items = Item.objects.all()
   return render(request, 'posapp/item_display.html', {'items': items})

def add_items(request):
   return render(request, "posapp/add_items.html")

def edit_items(request):
   return render(request, "posapp/edit_items.html")