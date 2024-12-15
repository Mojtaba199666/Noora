from rest_framework import serializers

from .models import Product_info


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_info
        fields = '__all__'

