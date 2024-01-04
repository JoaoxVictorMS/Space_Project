# ESTE ARQUIVO SERVE PARA CRIAR ESTRUTURAS DE DADOS EM FORMAS DE CLASSES E FUNÇÕES (ORIENTAÇÃO A OBJETOS).
# *********************************************************************************************************************
# O DJANGO IRÁ PEGAR TODAS ESTAS ESTRUTURAS E CRIAR TABELAS, NO BANCO DE DADOS, COM BASE NELAS. 
# *********************************************************************************************************************
# É AQUI QUE ENTRA O ORM (OBJECT RELATIONAL MAPPING), ONDE ELE IRÁ FAZER A PONTE ENTRE A APLICAÇÃO COM O BANCO DE DADOS
# *********************************************************************************************************************
# TODAS AS VEZES QUE É FEITA ALGUMA ALTERAÇÃO NESTE ARQUIVO É NECESSÁRIO QUE SEJA FEITO UM 'MAKEMIGRATIONS' E 'MIGRATE'
# *********************************************************************************************************************

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# A classe abaixo irá HERDAR uma outra classe chamada de: models.model 
class Fotografia(models.Model):
    ''' Classe que armazena todos os dados (atributos) referente as fotos '''


    # Lista de Tuplas. Deve ser uma Tupla pois o método CharField apenas entende esse tipo de estrutura
    # Esta estruta permite adcionar novas categorias de forma mais fácil.
    OPCOES_CATEGORIAS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
        ("GERAL", "Geral"),
    ]

    # CharField() é um campo que armazena um string, neste caso, o nome.
    # O tamanho máximo é 100 (max_lenght).
    # Não pode estarem vazias sem informações (null=False). 
    # O campo não pode ser vazio, como por exemplos strings vazias (blank=False).
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)

    # A função 'choices' (Field.choices) recebe uma lista como parâmetro e dentro desta lista contém as opções dadas pelo dev. 
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')

    # TextField() Armazena um conjunto arbitrário de caracteres de texto, podendo haver várias linhas e parágrafos
    descricao = models.TextField(null=False, blank=False)

    # Nome da foto, e não a foto em si. Estrutura antiga
    '''
    foto = models.CharField(max_length=100, null=False, blank=False)
    '''


    # Nesta nova estrutura, as fotos são do tipo ImageField, podendo agora fazer upload de fotos.
    # fotos/%Y/%m/%d: Dentro da pasta fotos, existirá uma outra pasta com o ano de cadastro desse iten. Depois outra pasta com o mês e mais uma com o dia
    # blank=True. É possível de cadastrar uma foto sem a foto propiamente dito
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)



    # BooleanField(default=false). 
    # Todo item adiconado não vai, por padrão, ser adicionado no site. É preciso colocalo como publicado (True) para aparecer.
    # No site de Admin, aparece um certinho no atributo 'publicada'
    # Foi mudada de default=False para default=True pois quando o usuário publicar uma nova imagem(nova feature btw), ela ja será publicada. O Admin decide se vai despublica-la ou não
    publicada = models.BooleanField(default=True)

    # Adicona a data de publicação da foto
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False) 

    '''
    # Estrutura velha. Boa prática. Muito útil no terminal:
    def __str__(self):
    Devolve a representação de um objeto em formato de string
        return f"Fotografia [nome={self.nome}]"
    '''

    # Estrutura que associa o usuário a tabela de User do django
    # A chave estrangeira (ForeignKey) é a responsável por associar tabelas
    # O parâmetro da classe de ForeignKey "to=" é a responsável por dizer qul tabela será associada
    # Os demais parâmetros são as características do user
    # Quando o usuário for deletado ele será definido como NULL, portanto "null=" deve ser True. Não pode ser blank e o related_name localiza mais facilmente a tabela
    usuario = models.ForeignKey(
        to = User,
        on_delete= models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    # Nova estrutura. Na tela de admin, retornará apenas o nome da foto ao adicionar uma nova foto no banco de dados
    def __str__(self):
        ''' Retorna apenas o nome'''
        return self.nome
        
    
    

                     

