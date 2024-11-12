# stockapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.stock_data, name='stock_data'),
    path('list/<str:market>/', views.stock_list, name='stock_list'),
    path('list_global/<str:market>/', views.stock_list_global, name='stock_list_global'),
    path('detail/<str:stock_id>/', views.stock_detail, name='stock_detail'),
    path('history/<str:stock_id>/', views.stock_history, name='stock_history'),
]
