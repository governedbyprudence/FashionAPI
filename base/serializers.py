from rest_framework import serializers
from .models import fashion

class fashion_serializer(serializers.ModelSerializer):

    class Meta:
        model = fashion
        fields= "__all__"