from django.db import models
from django.utils import timezone


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Cafe(models.Model):
    TIPO_CHOICES = [
        ('Café Expresso', 'Café Expresso'),
        ('Café com Leite', 'Café com Leite'),
        ('Cappuccino', 'Cappuccino'),
        ('Mocha', 'Mocha'),
        ('Latte', 'Latte'),
    ]

    tipo = models.CharField(choices=TIPO_CHOICES, max_length=50)
    nome = models.CharField(max_length=100)
    tamanho_copo = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='cafe_images/', blank=True, null=True)
    disponivel = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ingrdiente = models.ForeignKey(Ingrediente, related_name='ingredientes', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


class Sobremesas(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.ImageField(upload_to='sobremesas/', blank=True, null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome


class Testemunho(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    disponivel = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.nome


class Contatenos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=50)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome