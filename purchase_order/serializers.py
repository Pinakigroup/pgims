from rest_framework import serializers
from .models import PurchaseBill

class PurchaseBillSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.supplier_name')
    class Meta:
        model = PurchaseBill
        fields = ['style_no', 'work_order', 'master_lc_sc', 'buyer_name', 'supplier']