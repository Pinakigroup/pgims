from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.remarks_read, name='remarks_read'),
    path('<int:pk>/', views.remarks_update, name='remarks_update'),
    path('delete/<int:pk>/', views.remarks_delete, name='remarks_delete'),
]