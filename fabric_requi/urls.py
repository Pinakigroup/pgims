from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.FabricRequiCreateView.as_view(), name='create'),
    path('', views.fabricRequi_read, name='fabricr_read'),
    path('report/', views.fabricReport_read, name='fr_report'),
    # path('', views.FabricRequiView.as_view(), name='fabricr_read'),
    path("bill/<billno>", views.FabricRequiBillView.as_view(), name="fr_bill"),
    path('delete/<int:pk>/', views.FabricRequiDeleteView.as_view(), name='fr_delete'),
]