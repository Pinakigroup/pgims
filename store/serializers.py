from rest_framework import serializers
from .models import StoreBill, StoreItem

# For Fabric
class StoreBillSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['fileno_po', 'buyer_name']
        
class StoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        # fields = ['quantity', 'size', 'style', 'color']
        fields = '__all__'
       
        
class StoreAccessoriesSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['fileno_po', 'style_no']