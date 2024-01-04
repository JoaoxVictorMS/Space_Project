# O Django possui um recursos de criação de formulários com base em models pré-existentes, basta informar com model será baseado

# Import da biblioteca de forms do django
from django import forms
# Import do model de Fotografia que será usado para criar o forms
from apps.galeria.models import Fotografia

# O recurso ModelForm é justamente usado para criar formulários com base em outros models
# No caso dos formulários de Login e Cadastro, foram utilizados apenas o "".Form" pois é um form criado do zero. 
class FotografiaForms(forms.ModelForm):
    ''' Classe que contém os objetos dos c '''
    class Meta:
        ''' Dados que referenciam a natureza da classe de FotografiaForms '''
        model = Fotografia
        #Todos os atributos do models de galeria irão aparecer para o usuário, menos o exclude
        # Agora só os admins vão deixar como publicada ou não 
        exclude =['publicada',]

        # Editando os nomes das labels do formulário através do dicionário, onde o valor é o novo nome
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data de registro',
            'usuario':'Usuário'
        }

        # Aqui estão definidas as classes do CSS que serão operadas em cada campo de models(E mais algumas coisas) 
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                # Formato que a data será escrita na tela
                format='%d/%m/%Y',
                # Atributos
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuarios': forms.TextInput(attrs={'class':'form-control'})
        }

