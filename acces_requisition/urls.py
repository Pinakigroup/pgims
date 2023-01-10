from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.AccesRCreateView, name='create'),
    path('', views.AccesRView.as_view(), name='ar_read'),
    path("bill/<billno>", views.AccesRBillView, name="ar_bill"),
    path('delete/<int:pk>/', views.AccesRDeleteView, name='ar_delete'),
]