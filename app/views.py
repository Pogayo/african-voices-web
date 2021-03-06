#!/usr/bin/python
import os
from subprocess import Popen, TimeoutExpired
from threading import Thread
from time import sleep
from uuid import uuid4

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


from django.template import RequestContext

from .forms import SynthesizeForm, AddLanguageForm
from .models import Language, SynthesizeRequestModel, Dataset, AddLanguage, Country, Synthesizer


def delete_audio(audio_path):
    sleep(30)
    os.remove(audio_path)


def index(request):
    context = {'languages': Language.objects.all(),
               'num_synthesizers': len(Synthesizer.objects.all()), "num_countries":len(Country.objects.all()), "num_langs":len(Language.objects.all()), "num_speakers": 14, "num_hours": 120}

    return render(request, 'app/index.html', context)


def datasets(request):
    datasets = Dataset.objects.all()
    languages = Language.objects.all()
    context = {'languages': languages, 'datasets' : datasets, 'num_languages': len(languages), 'num_datasets': len(datasets)}
    return render(request, 'app/datasets.html', context)


def execute_synthesis(context):
    script = "./synthesize.sh"
    proc = Popen([script, "-v", context['synth_id'], "-i", context['text'], "-o", context['output_file'], "-f",
                  context['audio_format']])
    try:
        outs, errs = proc.communicate(timeout=15)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()

@csrf_exempt
def language(request, lang_code_639_2):
    language = get_object_or_404(Language,lang_code_639_2=lang_code_639_2)
    synthesizer_ids = [(synth.flite_location, synth.synth_id) for synth in language.synthesizer_set.all()]
    form = SynthesizeForm(synthesizer_ids)
    #context = {'language': language, 'form': form , 'languages': Language.objects.all(), }

    # return render(request, 'app/language.html', context)
    req_context = {}
    req_context.update({'language': language, 'form': form , 'languages': Language.objects.all(), })

    if request.method == 'POST':
        context={}
        context['synth_id'] = request.POST.get('synth_id')
        context['text'] = request.POST.get("text")
        context['audio_format'] = request.POST.get("audio_format")

        field_is_empty = is_empty(context['audio_format']) or is_empty(context['text']) or is_empty(context['synth_id'])

        if field_is_empty:
            return render(request, 'app/synthesize.html', {**context, "errors": "Fields are empty"})

        SynthesizeRequestModel.objects.create(**context)
        name = "app/synthesized/" + uuid4().hex
        context['output_file'] = name
        execute_synthesis(context)

        context['output_file'] = name + "." + context['audio_format']
        # delete the file
        new_thread = Thread(target=delete_audio, args=("public/static/" + context['output_file'],))
        new_thread.start()

        req_context.update(context)


    return render(request, 'app/language.html', req_context )

@csrf_exempt
def synthesize(request):
    context = {}

    if request.method == 'POST':
        context['synth_id'] = request.POST.get('synth_id')
        context['text'] = request.POST.get("text")
        context['audio_format'] = request.POST.get("audio_format")

        field_is_empty = is_empty(context['audio_format']) or is_empty(context['text']) or is_empty(context['synth_id'])

        if field_is_empty:
            return render(request, 'app/synthesize.html', {**context, "errors": "Fields are empty"})

        SynthesizeRequestModel.objects.create(**context)

        context['output_file'] = "app/static/app/synthesized/" + uuid4().hex
        execute_synthesis(context)

        context['output_file'] = context['output_file'][4:] + "." + context['audio_format']
        # delete the file
        new_thread = Thread(target=delete_audio, args=("app/" + context['output_file'],))
        new_thread.start()

    else:
        print("GET here")

    context['languages'] = Language.objects.all()
    return render(request, 'app/synthesize.html', context)


def developers(request):
    context = {'languages': Language.objects.all(), }
    return render(request, 'app/developers.html', context)

@csrf_exempt
def languages(request):
    context = {}

    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['wikipedia_url'] = request.POST.get("wikipedia_url")
        context['comment'] = request.POST.get("comment")
        context['email'] = request.POST.get("email")

        AddLanguage.objects.create(**context)


    form = AddLanguageForm()
    context = {'languages': Language.objects.all(),  'form': form, 'num_languages': len(Language.objects.all())}
    return render(request, 'app/languages.html', context)

def contribute(request):
    context = {'languages': Language.objects.all(), }
    return render(request, 'app/contribute.html', context)

def smartphone(request):
    context = {'languages': Language.objects.all(), }
    return render(request, 'app/smartphone.html', context)


def is_empty(s):
    return not s or not s.strip()


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)