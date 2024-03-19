from . import views
from django.urls import path

urlpatterns = [
    path('order/', views.OrderList.as_view(), name='order_list'),
    path('order/<int:pk>', views.OrderDetail.as_view(), name='order_detail'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),
]
