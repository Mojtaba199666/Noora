from django.shortcuts import render
from rest_framework import viewsets
from .models import Product_info
from .serializer import ProductSerializer
from rest_framework.response import Response


class ProductViews(viewsets.ViewSet):
    def list(self, request):
        queryset = Product_info.objects.all()

        serializer_data = ProductSerializer(queryset, many=True)

        print(serializer_data)

        return Response(serializer_data.data)
