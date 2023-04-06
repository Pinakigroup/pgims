from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.PurchaseCreateView.as_view(), name='create'),
    path('', views.purchaseOrder_read, name='po_read'),
    path("bill/<billno>", views.PurchaseBillView.as_view(), name="po_bill"),
    path('delete/<int:pk>/', views.PurchaseDeleteView.as_view(), name='po_delete'),
]