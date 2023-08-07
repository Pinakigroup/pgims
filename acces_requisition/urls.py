from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.AccesRCreateView.as_view(), name='create'),
    path('', views.accesR_read, name='ar_read'),
    path('report/', views.accesReport_read, name='ari_report'),
    # path('', views.AccesRView.as_view(), name='ar_read'),
    path("bill/<billno>", views.AccesRBillView.as_view(), name="ar_bill"),
    path('delete/<int:pk>/', views.AccesRDeleteView.as_view(), name='ar_delete'),
]