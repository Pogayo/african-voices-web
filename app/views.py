#!/usr/bin/python

from django.shortcuts import render
from .models import Language
from subprocess import call

def index(request):
    context = {'name': 'There', 'place':'Alice in wonderland', 'languages': Language.objects.all() }

    try:
        execute_transcription()
    except BaseException as e:
        print(e)

    return render(request, 'app/index.html', context)


def execute_transcription():
    print("Executing bash command")
    script = "/Users/nelsonbassey/Development/others/african_voices/transcribe.sh"
    res = call(script, shell=True)
    print(res)