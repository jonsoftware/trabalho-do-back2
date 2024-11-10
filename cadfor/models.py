from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)


class Contato(models.Model):
    TIPO_CHOICES = [
        ('email', 'Email'),
        ('telefone', 'Telefone'),
    ]
    
    id_contato = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    detalhe = models.CharField(max_length=255)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='contatos')


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='produtos')
