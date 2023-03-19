from django import forms
from .models import Contatenos


class ContatenosForm(forms.ModelForm):
    class Meta:
        model = Contatenos
        fields = ['nome', 'email', 'telefone', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'email-bt', 'placeholder': 'Nome', 'nome': 'nome'}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder': 'Email', 'nome': 'email'}),
            'telefone': forms.TextInput(attrs={'class': 'email-bt', 'placeholder': 'Telefone', 'nome': 'telefone'}),
            'mensagem': forms.Textarea(attrs={'class': 'massage-bt', 'placeholder': 'Mensgem', 'nome': 'mensagem'}),
        }
