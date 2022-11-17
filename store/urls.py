from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.store_read, name='store_read'),
    path('<int:pk>/', views.store_update, name='store_update'),
    path('delete/<int:pk>/', views.store_delete, name='store_delete'),   
]