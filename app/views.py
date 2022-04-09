from django.shortcuts import render
from .models import Language

def index(request):
    context = {'name': 'There', 'place':'Alice in wonderland', 'languages': Language.objects.all(),
               'num_synthesizers':  20, "num_countries":  20, "num_langs":  11, "num_speakers":  14, "num_hours":  600 }
    return render(request, 'app/index.html', context)