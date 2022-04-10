#!/usr/bin/python

from subprocess import call

from django.shortcuts import render

from .models import Language


def index(request):
    context = {'name': 'There', 'place': 'Alice in wonderland', 'languages': Language.objects.all(),
               'num_synthesizers': 20, "num_countries": 20, "num_langs": 11, "num_speakers": 14, "num_hours": 600}

    try:
        execute_transcription()
    except BaseException as e:
        print(e)

    return render(request, 'app/index.html', context)


def datasets(request):
    return render(request, 'app/datasets.html')

def execute_transcription():
    print("Executing bash command")
    script = "/Users/nelsonbassey/Development/others/african_voices/transcribe.sh"
    res = call(script, shell=True)
    print(res)


def language(request, lang_code_639_2):
    context = {'language': Language.objects.get(lang_code_639_2=lang_code_639_2)}
    return render(request, 'app/language.html', context)
