from django import forms
from core.models import *

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['id', 'balance']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs['class'] = 'form-control'
        
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.fields['forename'].widget.attrs['class'] = 'form-control'
        self.fields['surname'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['id', 'creation_date', 'account']

    def __init__(self, *args, **kwargs):
        super(DepositForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        