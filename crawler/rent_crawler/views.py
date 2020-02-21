from django.shortcuts import render
from . import models
from . import serializers
from rest_framework_mongoengine import generics, viewsets
from django.http import HttpResponse


class male(viewsets.ModelViewSet):
        queryset = models.data.objects.all()
        serializer_class = serializers.dataSerializer
# class male_region_1(generics.ListCreateAPIView):
#         queryset = models.data.objects.filter(sex__contains = '男').filter(region_id = '1')
#         serializer_class = serializers.dataSerializer    
# class male_region_3(generics.ListCreateAPIView):
#         queryset = models.data.objects.filter(sex__contains = '男').filter(region_id = '3')
#         serializer_class = serializers.dataSerializer


