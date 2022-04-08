from django.shortcuts import render


def index(request):
    context = {'name': 'There', 'place':'Alice in wonderland'}
    return render(request, 'app/index.html', context)