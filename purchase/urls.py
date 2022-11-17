from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.purchase_read, name='purchase_read'),
    path('<int:pk>/', views.purchase_update, name='purchase_update'),
    path('delete/<int:pk>/', views.purchase_delete, name='purchase_delete'),   
]