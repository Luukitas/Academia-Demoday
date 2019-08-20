from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from demo.views import * 
from demo.usuario import *

#imports da usados para a pagina de perguntas
from . import views

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastrar', cadastrar),
    path('usuario/<int:id>', usuario),
    path('experiencia/<int:id>', experiencia),
    path('cad-empresa', cadastra_empresa),
    path('list-empresa/<int:id>', procura_empresa),
    path('empresa/<int:id>/<str:name>', pagina_empr),
    path('conteudo/<int:id>', conteudo),
    path('home',sobre_nos),
    path('configuracoes/<int:id>', configuracao),
    #url da pagina de perguntas
    path('pergunta/inserir', views.pergunta_inserir, name='pergunta_inserir'),
    path('pergunta/atualizar/<int:id>', views.pergunta_atualizar, name = 'pergunta_atualizar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)