from django import forms


class SynthesizeForm(forms.Form):
    AUDIO_FORMAT = [('mp3', 'mp3'),
                    ('wav', 'wav')]

    def __init__(self, synthesizers, *args, **kwargs):
        super(SynthesizeForm, self).__init__(*args, **kwargs)
        print(synthesizers)
        self.fields['text'] = forms.CharField(label='Input', required=True, widget=forms.Textarea(
            attrs={'name': 'body', 'rows': '10', 'cols': '80', 'placeholder': 'Enter text here...'}))
        self.fields['synth_id'] = forms.ChoiceField(label='Synthesizer', required=True,
                                        choices=tuple([ synthesizer for synthesizer in synthesizers]))
        self.fields['audio_format'] = forms.ChoiceField(label='Audio format', required=True, choices=self.AUDIO_FORMAT,
                                   widget=forms.RadioSelect)
