from rest_framework import serializers
from . import models


class IaResponseSerializar(serializers.ModelSerializer):
    class Meta:
        model = models.IaResponse
        fields = '__all__'


class AudioListSerializer(serializers.Serializer):
    audio_responses = serializers.ListField(
        child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def create(self, validated_data):
        folder = models.Folder.objects.create()
        audio_responses = validated_data.pop('audio_responses')
        response_objs = []
        for response in audio_responses:
            response_obj = models.IaResponse.objects.create(folder=folder, audio_response=response)
            response_objs.append(response_obj)

        return {'audio_responses': {}, 'folder': str(folder.uid)}
