from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.storeRequis_read, name='storeRequis_read'),
    path('<int:pk>/', views.storeRequis_update, name='storeRequis_update'),
    path('delete/<int:pk>/', views.storeRequis_delete, name='storeRequis_delete'),   
]