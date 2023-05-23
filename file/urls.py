from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.file_read, name='file_read'),
    path('<int:pk>/', views.file_update, name='file_update'),
    path('delete/<int:pk>/', views.file_delete, name='file_delete'),  
]