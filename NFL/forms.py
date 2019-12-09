
from django.forms import ModelForm
from .models import Format
class Form(ModelForm):
    class Meta:
        model = Format
        fields = '__all__'
