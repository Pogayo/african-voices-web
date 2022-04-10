from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datasets', views.datasets, name='datasets'),
    path('synthesizers', views.synthesizers, name='synthesizers'),

]
