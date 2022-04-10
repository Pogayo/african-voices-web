from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datasets', views.datasets, name='datasets'),
    path('language/<str:lang_code_639_2>', views.language, name='language'),

]
