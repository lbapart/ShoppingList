from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='items'),
    path('item/<int:pk>/', views.ItemDetailed.as_view(), name='item-detailed'),
    path('item-create/', views.ItemCreate.as_view(), name='item-create'),
]