from rest_framework import serializers
from . import models


class IaResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.IaResponse
        fields = '__all__'
