from django.shortcuts import render


def index(request):
    context = {'data': 'data'}
    return render(request, 'app/index.html', context)