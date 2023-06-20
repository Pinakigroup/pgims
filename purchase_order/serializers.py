from rest_framework import serializers
from .models import PurchaseBill

class PurchaseBillSerializer(serializers.ModelSerializer):
    # buyer_name = serializers.CharField(source='buyer_name.buyer_name.name')
    class Meta:
        model = PurchaseBill
        fields = ['style_no', 'work_order', 'master_lc_sc', 'buyer_name']