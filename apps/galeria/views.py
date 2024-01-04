

from django.shortcuts import render, get_object_or_404, redirect
# Importe a forma como será feita a comunicação com a página web ( Não usado )
from django.http import HttpResponse
# Renomeação de 'galeria.models' para 'apps.galeria.models' pois criei a pasta de apps, mudança de referência
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

# O parâmetro indica para a função que será enviado uma requisição
def index(request):
    ''' Respode a requisição da página principal, a index '''
    
    # Verifica se o usuário não está logado. Caso não esteja, será redirecionado para a tela de login
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect ('login')

    # Busca todos os objetos presentes no banco de dados
    # Ná variável abaixo, foi utlizado a função all() que puxava todos os objetos do banco de dados.
    # Agora, graças a função filter(), será buscado apenas os objetos que contém o campo 'publicada' como True
    # As fotos aparecerão em ordem de publicação -> order_by()
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    # A função render pode também enviar informações através de dicionários.
    # render renderiza a página web solicitada.
    # render sempre recebe o parâmetro request primeiro.
    return render(request, 'galeria/index.html', {"cards": fotografias})


    '''
    # Estrutura de dados chamada de DICIONÁRIO
    # Os dicionários são coleções de itens e seus elementos são armazenados de forma não ordenada. Seus elementos contém uma chave e valor.
    # No exemplo abaixo criamos um dicionário que dentro dele possuí outros dicionários onde armazenam os dados que uma imagem tem.
    # Cada um desses dicionários possui seu id, no caso os números, que são as chaves para os valores que são outros dicionários
    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescopse.org / NASA / James Webb"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
}
    '''

    


def imagem(request, foto_id):
    ''' Responde a requisição das imagens presentes na página principal '''

    # Instância da view de imagem. Ela recebe, além do request da página, o id de uma foto.
    # Essa variável manipula o valor do foto_id para então referencialo ao objeto foto
    # get_object_or_404() é uma função que ou puxa o objeto ou devolve um 404, ou seja, não encontrado.
    # pk=foto_id refere-se ao primary key do banco de dados, que no caso é um número, onde estão localizadas ao fotos.
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    # A estrutura {"fotografia": fotografia} devolve ao usuário o objeto que faz referência ao id particular dele. 
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    ''' Responde a requisição feita através do campo de busca '''

    # Verifica se o usuário não está logado. Caso não esteja, será redirecionado para a tela de login
    
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect ('login')
    
    # Busca todos os objetos presentes no banco de dados
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    # Verifica se o termo "buscar" está sendo passada nas informações via url. Tais informações estão presentes em request.GET
    if "buscar" in request.GET:
        # Puxa o nome colocado no campo de busca da aplicação através do request.GET['buscar'], fazendo referência a tag name= do input da linha 10 em _menu.html
        nome_a_buscar = request.GET['buscar']
        # Verifica se de fato conseguiu algum nome que bate com o nome da imagem
        if nome_a_buscar:
            # Devolve a imagem com o nome igual ou parecido com o nome colocado no campo de busca. nome__icontains=nome_a_buscar realiza esta função
            # Colocar os dois underlines '__' na frente de uma variável criada, cria uma relação entre a variável e o método subsequente colocado, no caso o icontains
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    # Mudança de "galeria/buscar.html" para "galeira/index.html"
    # Não é mais necessário o "buscar.html" pois a view de filtro ja faz isso por ele
    return render(request, "galeria/index.html", {"cards":fotografias})

def nova_imagem(request):
    ''' Função de adição de imagem '''

     # Verifica se o usuário não está logado. Caso não esteja, será redirecionado para a tela de login
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect ('login')

    form = FotografiaForms
    # Verifica se as informações são pasadas pelo método POST e, caso sejam, as mesmas serão passadas para dentro da instância form de FotografiaForm
    if request.method == 'POST':
        # Nova instância de FotografiaForms mas recebendo as informações de POST (request.POST) e arquivos (request.FILES)
        form = FotografiaForms(request.POST, request.FILES)
        # Valida o formulário, se for válido, as informações serão salvas no banco de dados (model de Fotografia), será impressa uma mensagem de success e a aplicação será redirecionada para o index.html
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    # Passando a instância do formulário de FotografiaForms, através do dicionários, para o template
    return render(request, 'galeria/nova_imagem.html', {'form':form})

# Recebe também o id a foto pois só com o id ela pode ser encontrada
def editar_imagem(request, foto_id):
    ''' Função de edição das informações da imagem '''
    # Instância de Fotografia que busca os objetos do model de Fotografia, passando o id da foto
    fotografia = Fotografia.objects.get(id=foto_id)
    # Coloca-se as informações do objeto pego acima dentro do formulário
    form = FotografiaForms(instance=fotografia)


    if request.method == 'POST':
        # Mudança das informações novas editardas pelo usuário, pelas velhas
        # Essa instância são as novas informações
        # "instance=fotografia" existe pois aquilo que não for mudado será pego de fotografia 
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    # Retorno do formulário no html
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})


def deletar_imagem(request, foto_id):
    ''' Função de deleção de imagem '''
    # Instância de Fotografia que busca os objetos do model de Fotografia, passando o id da foto, e portanto, todas as suas informações
    fotografia = Fotografia.objects.get(id=foto_id)
    # Deleção da fotografia
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')


def filtro(request, categoria):
    ''' Função de filtragem de imagem '''
    # categoria=categoria 
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    # Retorna o index juntamente com o card(fotografia) corresponente ao filtro
    return render(request, 'galeria/index.html', {"cards":fotografias})