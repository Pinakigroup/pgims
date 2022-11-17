from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.supplier_read, name='supplier_read'),
    path('<int:pk>/', views.supplier_update, name='supplier_update'),
    path('delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),   
]