from random import choices
from .models import Movie
from django import forms


class MovieForm(forms.ModelForm):
    CHOICES = (('코미디','코미디'),('공포','공포'),('로맨스','로맨스'))
    genre = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Movie
        fields = '__all__'
        
        widgets = {
            'score':forms.NumberInput(attrs={
                'max':5,
                'step':0.5,
                'min':0.5,
            }),
            'release_date': forms.DateInput(attrs={
                'type':'date',
            }),
        }