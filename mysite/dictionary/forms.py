from django.forms.models import ModelForm
from .models import Dict


class WordForm(ModelForm):
    class Meta:
        model = Dict
        fields = '__all__'