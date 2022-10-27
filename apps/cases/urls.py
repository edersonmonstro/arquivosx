from django.urls import path

#now import the views.py file into this code
from . import views

urlpatterns = [
    path('',views.list),
    path('list/',views.list),
    path('create/',views.create),
    path('<id>', views.detail),
    path('<id>/update', views.update, name='case_update'),
    #path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('<id>/delete', views.delete),
    path('update/', views.updaterecord),
    path('previewnext/', views.previewnext),
]
 