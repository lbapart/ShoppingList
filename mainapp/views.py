from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Purchase

class ShoppingList(ListView):
    model = Purchase

class ItemDetailed(DetailView):
    model = Purchase
    template_name = 'mainapp/pur'

    