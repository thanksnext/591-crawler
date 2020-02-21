from rest_framework_mongoengine import serializers
from . import models

class dataSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.data
        fields = '__all__' #這個是將所有的欄位都序列化