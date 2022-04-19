from django import forms
from django.forms import ModelForm, Textarea, Form
from .models.synthesizer import *
from django.utils.translation import gettext_lazy as _




class SynthesizeForm(Form):
    AUDIO_FORMAT = [('mp3', 'mp3'),
                ('wav', 'wav')]
    def __init__(self, synthesizers, *args, **kwargs):

        super(SynthesizeForm, self).__init__(*args, **kwargs)
        # self.fields['synth_id'].choices = tuple([synthesizer for synthesizer in synthesizers])
            # [(synthesizer.id, synthesizer.name) for synthesizer in synthesizers] recommended by copilot

        self.fields['text'] = forms.CharField(label='Input', required=True, widget=forms.Textarea(
            attrs={'name': 'body', 'rows': '10', 'cols': '80', 'placeholder': 'Enter text here...', 'class':'form-control'}))
        self.fields['synth_id'] = forms.ChoiceField(label='Synthesizer', required=True,
                                                    choices=tuple([synthesizer for synthesizer in synthesizers]), widget=forms.Select(
                                                    attrs={'class':'form-control'}))
        self.fields['audio_format'] = forms.ChoiceField(label='Audio format', required=True, choices=self.AUDIO_FORMAT, widget=forms.RadioSelect)

    class Meta:
        # model = SynthesizeRequestModel
        # fields = ['text', 'synth_id', 'audio_format']
        # exclude = ('uuid', 'created_at', 'updated_at',)

        labels = {
            'text': _('Text'),
            'synth_id': _('Synthesizer'),
            'audio_format': _('Audio format'),
        }
        help_texts = {
            'text': _('Some useful help text.'),
        }
        error_messages = {
            'text': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'text': Textarea(attrs={'name': 'body', 'rows': '10', 'cols': '80', 'placeholder': 'new stuff...'}),
        }

#
# class SynthesizeForm(forms.Form):
#     AUDIO_FORMAT = [('mp3', 'mp3'),
#                     ('wav', 'wav')]
#
#     def __init__(self, synthesizers, *args, **kwargs):
#         super(SynthesizeForm, self).__init__(*args, **kwargs)
#         print(synthesizers)
#         self.fields['text'] = forms.CharField(label='Input', required=True, widget=forms.Textarea(
#             attrs={'name': 'body', 'rows': '10', 'cols': '80', 'placeholder': 'Enter text here...'}))
#         self.fields['synth_id'] = forms.ChoiceField(label='Synthesizer', required=True,
#                                         choices=tuple([ synthesizer for synthesizer in synthesizers]))
#         self.fields['audio_format'] = forms.ChoiceField(label='Audio format', required=True, choices=self.AUDIO_FORMAT,
#                                    widget=forms.RadioSelect)
