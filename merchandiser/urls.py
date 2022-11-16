from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.merchandiser_read, name='merchandiser_read'),
    path('<int:pk>/', views.merchandiser_update, name='merchandiser_update'),
    path('delete/<int:pk>/', views.merchandiser_delete, name='merchandiser_delete'),   
]