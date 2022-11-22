from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.storeRec_read, name='storeRec_read'),
    path('<int:pk>/', views.storeRec_update, name='storeRec_update'),
    path('delete/<int:pk>/', views.storeRec_delete, name='storeRec_delete'),   
]