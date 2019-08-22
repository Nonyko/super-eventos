from django.forms import ModelForm, Textarea, DateTimeInput, TextInput
from .models import Evento
from .widgets import BootstrapDateTimePickerInput

class EventoForm(ModelForm):
     class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'startdate', 'enddate', 'local']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'},),
            'descricao': Textarea(attrs={'class': 'form-control'}),
            'startdate': BootstrapDateTimePickerInput(),
            'enddate': BootstrapDateTimePickerInput(),
            'local': TextInput(attrs={'class': 'form-control'}),
        }
