from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import StoreBillDetailView, StoreAccessoriesDetailView

urlpatterns = [
    path('create/', views.StoreCreateView.as_view(), name='create'),
    path('', views.store_read, name='store_read'),
    path('report/', views.storeReport_read, name='store_report'),
    path("bill/<billno>", views.StoreBillView.as_view(), name="store_bill"),
    path('delete/<int:pk>/', views.store_delete, name='store_delete'),
    
    path('store/<str:work_order>/', StoreBillDetailView.as_view(), name='store_detail'),
    path('store/accessories/<str:work_order>/', StoreAccessoriesDetailView.as_view(), name='store_detail'),
]