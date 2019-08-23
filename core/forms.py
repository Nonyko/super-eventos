from django.forms import ModelForm, DateTimeField, Textarea, DateTimeInput, TextInput
from .models import Evento
from .widgets import BootstrapDateTimePickerInput


class EventoForm(ModelForm):
    startdate = DateTimeField(widget=BootstrapDateTimePickerInput(format='%d/%m/%Y %H:%M'),
                            input_formats=('%d/%m/%Y %H:%M',))
    enddate = DateTimeField(widget=BootstrapDateTimePickerInput(format='%d/%m/%Y %H:%M'), input_formats=('%d/%m/%Y %H:%M',))

    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'startdate', 'enddate', 'local']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'},),
            'descricao': Textarea(attrs={'class': 'form-control'}),
            'local': TextInput(attrs={'class': 'form-control'}),
        }



