from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.fabricRequis_read, name='fabricRequis_read'),
    path('<int:pk>/', views.fabricRequis_update, name='fabricRequis_update'),
    path('delete/<int:pk>/', views.fabricRequis_delete, name='fabricRequis_delete'),   
]