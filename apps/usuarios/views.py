from django.shortcuts import render, redirect
# Renomeação de 'usuarios.forms' para 'apps.usuarios.forms' pois criei a pasta de apps, mudança de referência
from apps.usuarios.forms import LoginForms, CadastroForms
# Importação da tabela de User que fica dentro do própio django
from django.contrib.auth.models import User
from django.contrib import auth # Biblioteca de autenticações
from django.contrib import messages # Biblioteca de mensagens de erro, por exemplo

# Retorno das requisições das páginas de login e cadastro (Rotas)
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        # Verifica se os dados do formulário são válidos
        if form.is_valid():
            # Traz os forms de nome_login e senha
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        # Autenticação do usuário, passando a requisição, login e senha
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha,
        )
        
        # Verifica se a variável usuario retornou None, coisa que não deve acontecer
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index')
        # Mas caso retornou None, o login não será efetuado e a palicação o redireciona para a tela inicial
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')

    # As informações do objeto instânciado acima, anteriormente criadas em views.py, no campo LoginForms, são passadas para o login.html através do dicionário chave-valor
    return render(request, "usuarios/login.html", {"form" : form})

def cadastro(request):
    form = CadastroForms()

    # Caso ocorra uma solitação do tipo POST, isto é, o usuário colocar suas informações de login e senha, será renderizado a tela explícita na variável form
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        #Verifica se as informações do formulário são válidas
        if form.is_valid():
            '''
            ------------------------------------------------------------------------------------------
            A ESTRUTURA ABAIXO É A VALIDAÇÃO DO FORMULÁRIO DE CADASTRO ANTIGA, A NOVA ESTÁ EM forms.py
            ------------------------------------------------------------------------------------------
            # A estrutura abaixo verifica se os valores de senha_1 e senha_2 são diferentes
                # A maneira mostrada abaixo é como se usa os valores do formulario: form[form1].value()
                if form["senha_1"].value() != form["senha_2"].value():
                    messages.error(request, "As senhas não são iguais")
                    return redirect('cadastro') 
            '''
            
            # As informações colocadas nos formulários pelo usuário, através do método POST, são armazenadas nas variáveis abaixo
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value() 

            # Verifica se há algum outro usuário com o mesmo nome, caso exista ele retorna para a página de cadastro
            # A tag username recebe esse nome pois no banco de dados a coluna de login é nomeada por username
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existe")
                return redirect('cadastro')
            
            # Criação do usuário com as informações colcadas pelo mesmo e depois salvas pelo usuarios.save()
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            # Após a criação, a aplicação o redirecionará para a tela de login
            return redirect('login')

    # As informações do objeto instânciado acima, anteriormente criadas em views.py, no campo LoginForms, são passadas para o login.html através do dicionário chave-valor
    return render(request, "usuarios/cadastro.html", {"form" : form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    # Apenas as pessoas logadas poderão ver as fotos do site, quando estiver deslogado não será possível, por isso retorna a tela de login
    return redirect('login')