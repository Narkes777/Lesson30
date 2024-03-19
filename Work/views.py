from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from .models import Order
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class OrderList(ListView):
    model = Order
    context_object_name = 'Order'

class OrderDetail(DetailView):
    model = Order
    context_object_name = 'Order'

class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('order_list')

class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('order_list')

class OrderDelete(DeleteView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('order_list')
    template_name = 'Work/order_form.html'


