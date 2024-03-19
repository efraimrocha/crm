from django import forms
from .models import Customer

# Insere a classe date no formulário para o campo data de nascimento.
class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email  = forms.EmailField(label="Email")
    birth_date = forms.DateField(label="Data de nascimento", widget=DateInput())
    area_code = forms.CharField(label="DDD")
    phone_number = forms.CharField(label="Telefone")
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = (
            "first_name",  
            "last_name",   
            "email",        
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )