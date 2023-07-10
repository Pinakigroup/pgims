from rest_framework import serializers
from .models import PurchaseBill

class PurchaseBillSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.supplier_name')
    fileno_po = serializers.CharField(source='fileno_po.file')
    class Meta:
        model = PurchaseBill
        fields = ['style_no', 'fileno_po', 'master_lc_sc', 'buyer_name', 'supplier']