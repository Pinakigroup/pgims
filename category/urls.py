from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.category_read, name='category_read'),
    path('<int:pk>/', views.category_update, name='category_update'),
    path('delete/<int:pk>/', views.category_delete, name='category_delete'),   
]