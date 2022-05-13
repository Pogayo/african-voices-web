from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datasets', views.datasets, name='datasets'),
    path('language/<str:lang_code_639_2>', views.language, name='language'),
    path('synthesize', views.synthesize, name='synthesize'),
    path('languages', views.languages, name='languages'),
    path('flite', views.flite, name='flite'),
    path('contribute', views.contribute, name='contribute'),

]
