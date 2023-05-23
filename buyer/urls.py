from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.buyer_read, name='buyer_read'),
    path('<int:pk>/', views.buyer_update, name='buyer_update'),
    path('delete/<int:pk>/', views.buyer_delete, name='buyer_delete'),  
]