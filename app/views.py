from django.shortcuts import render
from .models import Language

def index(request):
    context = {'name': 'There', 'place':'Alice in wonderland', 'languages': Language.objects.all() }
    return render(request, 'app/index.html', context)