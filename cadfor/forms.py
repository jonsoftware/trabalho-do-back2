from django import forms
from .models import Fornecedor, Contato, Produto

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['tipo', 'detalhe']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']