from rest_framework.serializers import serializer
from AudioResponse.models import IaAudioResponse


class IaAudioResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IaAudioResponse
        fields = ('id',
                  'binaryContent',
                  'stringResponse')
