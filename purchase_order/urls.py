from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import PurchaseBillDetailView

urlpatterns = [
    path('create/', views.PurchaseCreateView.as_view(), name='create'),
    path('', views.purchaseOrder_read, name='po_read'),
    path('report/', views.woReport_read, name='wo_report'),
    path("bill/<billno>", views.PurchaseBillView.as_view(), name="po_bill"),
    path('delete/<int:pk>/', views.purchase_delete, name='po_delete'), 
    # path('api/purchase/<int:pk>/', PurchaseBillDetailView.as_view(), name='person_detail'), 
    path('purchase/<int:pk>/', PurchaseBillDetailView.as_view(), name='purchase_detail'),
]