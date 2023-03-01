from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='purchase'),
    path('purchase/<int:pk>', views.ItemDetailed.as_view(), name='purchase-detailed')
]