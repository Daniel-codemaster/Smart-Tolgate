from django import forms
from core.models import *

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['number_plate'].widget.attrs['class'] = 'form-control'   
        self.fields['type_id'].widget.attrs['class'] = 'form-control'     
        self.fields['make'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['class'] = 'form-control'     
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['class'] = 'form-control'
        