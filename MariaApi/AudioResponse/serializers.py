from rest_framework.serializers import serializers
from AudioResponse.models import IaAudioResponse


class IaAudioResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IaAudioResponse
        fields = ('id',
                  'binaryContent',
                  'stringResponse')
