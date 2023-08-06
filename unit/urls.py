from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.unit_read, name='unit_read'),
    path('<int:pk>/', views.unit_update, name='unit_update'),
    path('delete/<int:pk>/', views.unit_delete, name='unit_delete'),
]