from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.stock_read, name='stock_read'),
    path('create/', views.StockCreateView.as_view(), name='new'),
    path('<int:pk>/edit', views.StockUpdateView.as_view(), name='stock_update'),
    path('delete/<int:pk>/', views.stock_delete, name='stock_delete'),
]