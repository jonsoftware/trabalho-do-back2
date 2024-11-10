"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cadfor.views import (
    FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView,
    ContatoCreateView, ContatoUpdateView, ContatoDeleteView, ProdutoCreateView, ProdutoUpdateView, 
    ProdutoDeleteView, FornecedorDetailView, ContatoListView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", FornecedorListView.as_view(), name="fornecedor_list"),
    path("fornecedor/create/", FornecedorCreateView.as_view(), name="fornecedor_create"),
    path("fornecedor/<int:pk>/update/", FornecedorUpdateView.as_view(), name="fornecedor_update"),
    path("fornecedor/<int:pk>/delete/", FornecedorDeleteView.as_view(), name="fornecedor_delete"),
    path("fornecedor/<int:pk>/", FornecedorDetailView.as_view(), name="fornecedor_detail"),
    
    path('contato/list/<int:pk>/', ContatoListView.as_view(), name='contato_list'),
    path("contato/create/", ContatoCreateView.as_view(), name="contato_create"),
    path("contato/<int:pk>/update/", ContatoUpdateView.as_view(), name="contato_update"),
    path("contato/<int:pk>/delete/", ContatoDeleteView.as_view(), name="contato_delete"),

    path("produto/create/", ProdutoCreateView.as_view(), name="produto_create"),
    path("produto/<int:pk>/update/", ProdutoUpdateView.as_view(), name="produto_update"),
    path("produto/<int:pk>/delete/", ProdutoDeleteView.as_view(), name="produto_delete"),
]
