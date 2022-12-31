from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.StoreCreateView.as_view(), name='create'),
    path('', views.StoreView.as_view(), name='store_read'),
    path("bill/<billno>", views.StoreBillView.as_view(), name="store_bill"),
]