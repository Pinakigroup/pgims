from rest_framework import serializers
from .models import StoreBill, StoreItem

# For Fabric
class StoreBillSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['fileno_po', 'buyer_name']
        
class StoreItemSerializer(serializers.ModelSerializer):
    stock = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()

    def get_stock(self, instance):
        return {
            "id": instance.stock.id if instance.stock else '',
            "name": instance.stock.name if instance.stock else ''
        }

    def get_unit(self, instance):
        return {
            "id": instance.unit.id if instance.unit else '',
            "unit": instance.unit.unit if instance.unit else ''
        }

    class Meta:
        model = StoreItem
        # fields = ['quantity', 'size', 'style', 'color']
        fields = '__all__'
       
        
class StoreAccessoriesSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['fileno_po', 'style_no']