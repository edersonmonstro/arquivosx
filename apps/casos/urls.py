from django.urls import path

#now import the views.py file into this code
from . import views

urlpatterns = [
    path('',views.index),
    path('list/',views.list),
    path('create/',views.create),
    path('<id>', views.detail),
    path('<id>/update', views.update),
    path('<id>/delete', views.delete),
]
 