"""pgims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
        
    path('category/', include('category.urls')),
    path('stock/', include('stock.urls')),
    path('product/', include('product.urls')),
    path('merchandiser/', include('merchandiser.urls')),
    path('supplier/', include('supplier.urls')),
    path('purchase/', include('purchase.urls')),
    path('store/', include('store.urls')),
    path('store_receiver/', include('store_receiver.urls')),
    path('store_requisition/', include('store_requisition.urls')),
    path('fabric_requisition/', include('fabric_requisition.urls')),
    path('accounts/', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
