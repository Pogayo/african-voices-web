from django import forms
from django.forms import ModelForm, Textarea, Form
from .models.synthesizer import *
from django.utils.translation import gettext_lazy as _




class SynthesizeForm(Form):
    AUDIO_FORMAT = [('mp3', 'mp3'),
                ('wav', 'wav')]
    def __init__(self, synthesizers, *args, **kwargs):

        super(SynthesizeForm, self).__init__(*args, **kwargs)
        self.fields['text'] = forms.CharField(label='Input', required=True, widget=forms.Textarea(
            attrs={'name': 'body', 'rows': '10', 'cols': '80', 'placeholder': 'Enter text here...', 'class':'form-control'}))
        self.fields['synth_id'] = forms.ChoiceField(label='Choose synthesizer', required=True,
                                                    choices=tuple([synthesizer for synthesizer in synthesizers]), widget=forms.Select(
                                                    attrs={'class':'form-control'}))
        self.fields['audio_format'] = forms.ChoiceField(label='Audio format', required=True, choices=self.AUDIO_FORMAT, widget=forms.RadioSelect)

    class Meta:

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
class AddLanguageForm(Form):
    def __init__(self,*args, **kwargs):

        super(AddLanguageForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label='Name of language', required=True, widget=forms.TextInput( attrs={'name': 'name', 'placeholder': 'Enter language name...', 'class':'form-control'}))
        self.fields['wikipedia'] =  forms.URLField(label='Wikipedia url', required=False, widget=forms.URLInput( attrs={'name': 'wikipedia', 'placeholder': 'Enter wikipedia url...', 'class':'form-control'}))
        self.fields['comment'] = forms.CharField(label='Comment', required=False, widget=forms.Textarea(
            attrs={'name': 'body', 'rows': '5', 'cols': '80', 'placeholder': 'Any other info such as countries where it is spoken...',
                   'class': 'form-control'}))
        self.fields['email'] =  forms.EmailField(max_length = 200, widget = forms.EmailInput(attrs={'name': 'email', 'placeholder': 'Enter email...', 'class':'form-control'}))

