from rest_framework import serializers

from store.models import StoreItem
from .models import PurchaseBill, PurchaseItem

class PurchaseBillSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.supplier_name')
    fileno_po = serializers.CharField(source='fileno_po.file')
    
    class Meta:
        model = PurchaseBill
        # fields = ['style_no', 'fileno_po', 'master_lc_sc', 'buyer_name', 'supplier']
        fields = '__all__'
        

class PurchaseItemSerializer(serializers.ModelSerializer):
    stock = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    received_quantity = serializers.SerializerMethodField()

    def get_stock(self, instance):
        return {'id': instance.stock.id if instance.stock else '', 'name': instance.stock.name if instance.stock else ''}

    def get_unit(self, instance):
        return {'id': instance.unit.id if instance.id else '', 'unit': instance.unit.unit if instance.unit else ''}

    def get_received_quantity(self, instance):
        work_order = instance.billno.work_order if instance.billno else None
        if work_order:
            obj = StoreItem.objects.filter(billno__work_order__work_order=work_order,
                                           size=instance.size, style=instance.style, color=instance.color).first()
            if obj:
                return obj.received_quantity
        return 0

    class Meta:
        model = PurchaseItem
        # fields = ['quantity', 'size', 'style', 'color']
        fields = '__all__'

