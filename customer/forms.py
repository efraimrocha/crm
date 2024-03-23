from django import forms
from .models import Customer

# Insere a classe date no formulário para o campo data de nascimento.
class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_length": "Nome não pode ter mais de 30 caracteres"}
        )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "Sobrenome não pode ter mais de 50 caracteres"}
        )
    email  = forms.EmailField(label="Email")
    birth_date = forms.DateField(label="Data de nascimento", widget=DateInput()) # Adiciona o widget customizado para inseir a classe date ao campo.
    area_code = forms.RegexField(   # O RegexField é usado para validar um campo com base em expressões regulares.
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "Número de DDD inválido"}
        )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{9,15}$",
        error_messages={"invalid": "Número de telefone inválido"}
        )
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