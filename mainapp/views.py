from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Purchase
from django.urls import reverse_lazy

class ShoppingList(ListView):
    model = Purchase

class ItemDetailed(DetailView):
    model = Purchase
    template_name = 'mainapp/purchase_detail.html'

class ItemCreate(CreateView):
    model = Purchase
    fields = ['title', 'quantity', 'quantityType']
    success_url = reverse_lazy('items')

class ItemUpdate(UpdateView):
    model = Purchase
    fields = ['title', 'quantity', 'quantityType', 'completed']
    success_url = reverse_lazy('items')

class ItemDelete(DeleteView):
    model = Purchase
    success_url = reverse_lazy('items')