from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('updatemon/', views.updateMon, name='updatemon'),
        path('updateitem/', views.updateItem, name='updateitem'),
        path('updatemove/', views.updateMove, name='updatemove'),
        path('updatemoveset/', views.updateMoveset, name='updatemoveset'),
        path('makeimage/', views.makeImage, name='makeimage'),
        path('monlookup/', views.monLookup, name='monlookup'),
    ]
