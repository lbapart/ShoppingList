from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='items'),
    path('item/<int:pk>/', views.ItemDetailed.as_view(), name='item-detailed'),
    path('item-create/', views.ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>/', views.ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', views.ItemDelete.as_view(), name='item-delete'),
]