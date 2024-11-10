from django.shortcuts import render
from .models import Fornecedor, Contato, Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Views do Fornecedor
class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'cadfor/fornecedor_list.html'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = ["nome", "cnpj", "endereco", "telefone", "email"]
    success_url = reverse_lazy("fornecedor_list")

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email']
    success_url = reverse_lazy('fornecedor_list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor_list')

    # Sobrescreve o método post para adicionar lógica de exclusão dos contatos e produtos
    def post(self, request, *args, **kwargs):
        fornecedor = self.get_object()

        # Excluir todos os contatos e produtos relacionados
        Contato.objects.filter(fornecedor=fornecedor).delete()
        Produto.objects.filter(fornecedor=fornecedor).delete()

        # Excluir o fornecedor
        fornecedor.delete()
        return super().post(request, *args, **kwargs)  # Redireciona para 'fornecedor_list'


# Views do Contato
class ContatoCreateView(CreateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']

    # Retorna para a página anterior usando HTTP_REFERER/mantém na página de criação
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class ContatoListView(ListView):
    model = Contato
    template_name = 'cadfor/contato_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fornecedor_id = self.kwargs.get('pk')
        context['fornecedor'] = Fornecedor.objects.get(id_fornecedor=fornecedor_id)
        context['contatos'] = Contato.objects.filter(fornecedor=context['fornecedor'])
        context['fornecedor_id'] = fornecedor_id  # Passa o fornecedor_id para o template
        return context

class ContatoUpdateView(UpdateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']
    template_name = 'cadfor/contato_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fornecedor = self.object.fornecedor
        context['contatos'] = Contato.objects.filter(fornecedor=fornecedor)
        return context

    def get_success_url(self):
        return reverse_lazy('contato_list', kwargs={'pk': self.object.fornecedor.id_fornecedor})

class ContatoDeleteView(DeleteView):
    model = Contato

    def get_success_url(self):
        return reverse_lazy('contato_list', kwargs={'pk': self.object.fornecedor.id_fornecedor})


# Views do Produto
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')


# Detalhe do Fornecedor
class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'cadfor/fornecedor_detail.html'
    context_object_name = 'fornecedor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contatos'] = self.object.contatos.all()
        context['produtos'] = self.object.produtos.all()
        return context
