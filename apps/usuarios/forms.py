# ***** ESTE ARQUIVO FOI CRIADO JUSTAMENTE PARA MANIPULAR OS FORMULÁRIOS *****  
# O Django possui ferramentas para manipular formulários de forma mais eficiente e rápida, uma vez que tal recurso é muito utilizado em programação WEB
# A extensão forms é a resposável por isso, sendo possível editar os formulários sem precisar editar as labels no html diretamente
from typing import Any
from django import forms

class LoginForms(forms.Form):
    ''' Classe que contém os objetos dos campos de login e senha '''
    # Objeto que representa o campo de login
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        # O PasswordInput recebeu um parâmetro chamado de attrs. Nele foi colocado a estilização do campo de login
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: João Silva"
            }
        )
    )
    # Objeto que representa o campo de senha
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        # O parâmetro widget permte que editemos características dos Inputs
        # O PasswordInput recebeu um parâmetro chamado de attrs. Nele foi colocado a estilização do campo de senha
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    ''' Classe que contém os objetos dos campos de nome de cadastro, email, senha '''
    nome_cadastro = forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        # O PasswordInput recebeu um parâmetro chamado de attrs. Nele foi colocado a estilização do campo de login
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: joaosilva@xpto.com"
            }
        )
    )
    # Campo de senha para digitação inicial
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        # O parâmetro widget permite que editemos características dos Inputs
        # O PasswordInput recebeu um parâmetro chamado de attrs. Nele foi colocado a estilização do campo de senha
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )
    # Campo de senha para confirmação
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        # O parâmetro widget permte que editemos características dos Inputs
        # O PasswordInput recebeu um parâmetro chamado de attrs. Nele foi colocado a estilização do campo de senha
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha novamente"
            }
        )
    )

    # Boa prática o usu do CLEAN
    def clean_nome_cadastro(self):
        """ Valida se o nome do usuário possui espaço ou não """
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            else:
                return nome

    '''
    ---------------------------------------------------------------------------------------------------
    A ESTRUTURA ABAIXO É A VALIDAÇÃO DO FORMULÁRIO DE CADASTRO ANTIGA QUE FICAVA NO ARQUIVO DE views.py
    ---------------------------------------------------------------------------------------------------
    # A estrutura abaixo verifica se os valores de senha_1 e senha_2 são diferentes
        # A maneira mostrada abaixo é como se usa os valores do formulario: form[form1].value()
        if form["senha_1"].value() != form["senha_2"].value():
            messages.error(request, "As senhas não são iguais")
            return redirect('cadastro') 
    '''
    
    # Boa prática o usu do CLEAN
    # NOVA ESTRUTURA DE VALIDAÇÃO
    def clean_senha_2(self):
        """ Verifica se as senhas colocadas pelo usuário são iguais """
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        # Se as senhas existem
        if senha_1 and senha_2:
            # Se as senhas são diferentes
            if senha_1 != senha_2:
                # Usa o forms validator e não mais menssagens de erro
                raise forms.ValidationError("Senhas não são iguais")
            # Caso sejam iguais
            else:
                return senha_2
