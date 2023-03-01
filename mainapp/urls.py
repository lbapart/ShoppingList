from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='purchase')
]