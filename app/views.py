#!/usr/bin/python
import time
from subprocess import check_call
from uuid import uuid4

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import SynthesizeForm
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


def execute_transcription(context):
    print("Executing bash command")
    script = "./transcribe.sh"
    res = check_call([script, "-v", context['synth_id'], "-i", context['text'], "-o", context['output_file']])
    print(res)


def language(request, lang_code_639_2):
    language = Language.objects.get(lang_code_639_2=lang_code_639_2)
    synthesizer_ids = [(synth.flite_location, synth.synth_id) for synth in language.synthesizer_set.all()]
    context = {'language': language, 'form': SynthesizeForm(synthesizer_ids)}
    return render(request, 'app/language.html', context)


@csrf_exempt
def synthesize(request):
    context = {}
    if request.method == 'POST':
        context['synth_id'] = request.POST.get('synth_id')
        context['text'] = request.POST.get("text")
        context['audio_format'] = request.POST.get("audio_format")
        context['output_file'] = "app/static/app/synthesized/" + uuid4().hex + "." + "wav"
        execute_transcription(context)
        time.sleep(3)
        # TODO: convert the wav file to mp3
        # TODO: write a job to delete the wav files after a while
        context['output_file'] = context['output_file'][4:]

    return render(request, 'app/synthesize.html', context)
