from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='items'),
    path('login/', views.AppLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('item/<int:pk>/', views.ItemDetailed.as_view(), name='item-detailed'),
    path('item-create/', views.ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>/', views.ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', views.ItemDelete.as_view(), name='item-delete'),
]