#!/usr/bin/python
from subprocess import Popen, TimeoutExpired
from uuid import uuid4

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import SynthesizeForm
from .models import Language

def index(request):
    context = {'name': 'There', 'place': 'Alice in wonderland', 'languages': Language.objects.all(),
               'num_synthesizers': 20, "num_countries": 20, "num_langs": 11, "num_speakers": 14, "num_hours": 600}


    return render(request, 'app/index.html', context)


def datasets(request):
    return render(request, 'app/datasets.html')


def execute_synthesis(context):
    script = "./synthesize.sh"
    proc = Popen([script, "-v", context['synth_id'], "-i", context['text'], "-o", context['output_file'], "-f", context['audio_format']])
    try:
        outs, errs = proc.communicate(timeout=15)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()


def language(request, lang_code_639_2):
    language = Language.objects.get(lang_code_639_2=lang_code_639_2)
    synthesizer_ids = [(synth.flite_location, synth.synth_id) for synth in language.synthesizer_set.all()]
    context = {'language': language, 'form': SynthesizeForm(synthesizer_ids)}
    return render(request, 'app/language.html', context)


@csrf_exempt
def synthesize(request):
    context = {}
    form = SynthesizeForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and form.is_valid() :
        new_request = form.save()
        context['synth_id'] = new_request.synth_id
        context['text'] = new_request.text
        context['output_file'] =  "app/static/app/synthesized/" + uuid4().hex
        context['audio_format'] = new_request.audio_format

        # context['synth_id'] = request.POST.get('synth_id')
        # context['text'] = request.POST.get("text")
        # print("hehheheh", context['text'])
        # context['audio_format'] = request.POST.get("audio_format")
        # context['output_file'] = "app/static/app/synthesized/" + uuid4().hex
        execute_synthesis(context)


        # time.sleep(3)
        # TODO: write a job to delete the wav files after a while
        context['output_file'] = context['output_file'][4:]+"." + context['audio_format']
    else:
        print("form is not valid")
        print(form.errors)

    return render(request, 'app/synthesize.html', context)
