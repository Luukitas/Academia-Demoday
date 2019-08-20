from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from demo.models import Disciplina
#from demo.models import Ano
from demo.models import Framework
from demo.models import Area
from demo.models import Nivel

class Command(BaseCommand):
    help = 'script para popular as tabelas de dominio'

    disciplinas = ['Python', 'JavaScript', 'HTML', 'CSS', 'C++', 'C#', 'PHP']
    frameworks = ['Django', 'React', 'React Native', 'CWF', '.NET', 'Laravel']
    #anos = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    areas = ['Full-Stack', 'Front-end', 'Back-end', 'segurança da informação', 'DevOps', 'Games']
    niveis = ['Basico', 'Intermediario', 'Avançado', 'Ninja']

    def handle(self, *args, **options):
        self.popular_tabelas()
    
    def popular_tabelas(self):
        self.popular_tabela(Disciplina, self.disciplinas)
        #self.popular_tabela(Ano, self.anos)
        self.popular_tabela(Framework, self.frameworks)
        self.popular_tabela(Area, self.areas)
        self.popular_tabela(Nivel, self.niveis)
        self.stdout.write('Registros inseridos com sucesso!')


    def popular_tabela(self, objeto, lista):
        for descricao in lista:
            novo_objeto = self.criar_objeto(objeto, descricao)
            try:
                novo_objeto.save()
            except:
                    self.stdout.write('O registro "%s" já existe na base de dados' % descricao)

    def criar_objeto(self, objeto, descricao):
        if(objeto.__name__ == 'Disciplina'):
            return Disciplina(descricao = descricao)
        #if(objeto.__name__ == 'Ano'):
        #    return Ano(descricao = descricao)
        if(objeto.__name__ == 'Framework'):
            return Framework(descricao = descricao)
        if(objeto.__name__ == 'Area'):
            return Area(descricao = descricao)
        if(objeto.__name__ == 'Nivel'):
            return Nivel(descricao = descricao)