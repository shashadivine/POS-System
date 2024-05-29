from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.openpos, name="openpos"),
   path('item_display/', views.item_display, name="item_display"),
   path('add_items/', views.add_items, name="add_items"),
   path('edit_items/', views.edit_items, name="edit_items")
]

