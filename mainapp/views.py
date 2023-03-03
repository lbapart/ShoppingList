from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Purchase


class ShoppingList(LoginRequiredMixin, ListView):
    model = Purchase
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        return context

class ItemDetailed(LoginRequiredMixin, DetailView):
    model = Purchase
    template_name = 'mainapp/purchase_detail.html'
    
    def get(self, *args, pk, **kwargs):
        selectItemQuery = Purchase.objects.filter(pk=pk).values()
        if selectItemQuery:
            selectItemUserId = selectItemQuery[0]['user_id']
            if self.request.user.pk == selectItemUserId:
                return super(ItemDetailed, self).get(pk, *args, **kwargs)
        
        return HttpResponseForbidden('Forbidden')

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    fields = ['title', 'quantity', 'quantityType']
    success_url = reverse_lazy('items')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    fields = ['title', 'quantity', 'quantityType', 'completed']
    success_url = reverse_lazy('items')
    
    def get(self, *args, pk, **kwargs):
        selectItemQuery = Purchase.objects.filter(pk=pk).values()
        if selectItemQuery:
            selectItemUserId = selectItemQuery[0]['user_id']
            if self.request.user.pk == selectItemUserId:
                return super(ItemUpdate, self).get(*args, **kwargs)
        
        return HttpResponseForbidden('Forbidden')
            
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemUpdate, self).form_valid(form)

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    success_url = reverse_lazy('items')
    
    def get(self, *args, pk, **kwargs):
        selectItemQuery = Purchase.objects.filter(pk=pk).values()
        if selectItemQuery:
            selectItemUserId = selectItemQuery[0]['user_id']
            if self.request.user.pk == selectItemUserId:
                return super(ItemDelete, self).get(pk, *args, **kwargs)
        
        return HttpResponseForbidden('Forbidden')
    
    def delete(self, request, *args, pk, **kwargs):
        selectItemQuery = Purchase.objects.filter(pk=pk).values()
        if selectItemQuery:
            selectItemUserId = selectItemQuery[0]['user_id']
            if self.request.user.pk == selectItemUserId:
                return super(ItemDelete, self).delete(request, *args, **kwargs)
        
        return HttpResponseForbidden('Forbidden')

class AppLoginView(LoginView):
    template_name = 'mainapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = False
    
    def get_success_url(self) -> str:
        return reverse_lazy('items')

class RegisterView(FormView):
    template_name = 'mainapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('items')
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        
        return super(RegisterView, self).get(*args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
