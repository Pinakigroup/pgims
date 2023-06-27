from rest_framework import serializers
from .models import StoreBill

class StoreBillSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['work_order', 'buyer_name']
        
        
class StoreAccessoriesSerializer(serializers.ModelSerializer):
    # file_no_store = serializers.CharField(source='file_no_store.fileno_po.file')  # This line use for get file no (not file id)
    class Meta:
        model = StoreBill
        fields = ['style_no']