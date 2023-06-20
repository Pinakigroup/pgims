from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    buyer_name = serializers.CharField(source='buyer_name.name')
    class Meta:
        model = File
        fields = ['master_lc_sc', 'buyer_name']