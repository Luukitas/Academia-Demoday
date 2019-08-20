from django.db import models

# Create your models here.

class Pessoa(models.Model):

    nome = models.CharField(
        max_length=255,
        verbose_name='nome',
        null=True,
        blank=True,        
    )

    email = models.EmailField(
        max_length=255,
        verbose_name= 'e-mail',
        unique=True,
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='senha'
    )

    profissao = models.CharField(
        max_length=255,
        verbose_name='profissão',
        null=True,
        blank=True,
    )

    experiencia = models.CharField(
        max_length=255,
        verbose_name='experiencia',
        null=True,
        blank=True,
    )

    img_perfil = models.ImageField(
        upload_to='images_pessoa/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Exp_pessoa(models.Model):

    experiencia = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    valores = models.TextField(
        verbose_name='valores',
        null=True,
        blank=True
    )


class Empresa(models.Model):

    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade',
        blank=True,
        null=True
    )

    rua = models.CharField(
        max_length=255,
        verbose_name='Rua',
        blank=True,
        null=True
    )

    numero = models.CharField(
        max_length=255,
        verbose_name='Numero',
        blank=True,
        null=True
    )

    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento',
        blank=True,
        null=True
    )

    img_perfil = models.ImageField(
        upload_to='images/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome',
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='Senha',
    )

    estado = models.CharField(
        verbose_name='Estado',
        choices=ESTADO,
        max_length=255,
        blank=True,
        null=True
    )

    atuacao = models.CharField(
        max_length=255,
        verbose_name='Atuacao',
        blank=True,
        null=True
    )

    cpf = models.CharField(
        max_length=20,
        verbose_name='Cpf',
        blank=True,
        null=True
    )

    descricao = models.TextField(
        verbose_name='Descricao',
        blank=True,
        null=True
    )

    linguagens = models.TextField(
        verbose_name='Linguagens',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome




#Models do questionario 
class Disciplina(models.Model): #Linguagem da pergunta
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self): #coloca as opções da tabela a serem dmonstradas para o usuario
        return self.descricao

#class Ano(models.Model):
   #descricao = models.CharField(max_length = 4, unique = True)

    #def __str__(self):
        #return self.descricao

class Framework(models.Model): #A pergunta é sobre django, python, programação pura?
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Nivel(models.Model): #Nivel da pergunta, basico, intermediário ou avançado?
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Area(models.Model):  #Tópico, é voltado a games?Servidores, segurança da informação?
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Pergunta(models.Model):
    texto = models.TextField()
    respondida = models.BooleanField(default = False)
    correta = models.BooleanField(default = False)
    disciplina = models.ForeignKey('Disciplina', on_delete = models.CASCADE, related_name = 'pergunta', null=True, blank=True)
    #ano = models.ForeignKey('Ano', on_delete = models.CASCADE, related_name = 'pergunta')
    area = models.ForeignKey('Area', on_delete = models.CASCADE, related_name = 'pergunta', null=True, blank=True)
    nivel = models.ForeignKey('Nivel', on_delete = models.CASCADE, related_name = 'pergunta', null=True, blank=True)
    Framework = models.ForeignKey('Framework', on_delete = models.CASCADE, related_name = 'pergunta')


class Alternativa(models.Model):
    texto = models.TextField()
    correta = models.BooleanField(default = False)
    selecionada = models.BooleanField(default = False)
    pergunta =  models.ForeignKey('Pergunta', on_delete = models.CASCADE, related_name = 'alternativa')