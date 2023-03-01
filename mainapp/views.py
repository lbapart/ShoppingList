from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Purchase

class ShoppingList(ListView):
    model = Purchase
    