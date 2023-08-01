import shutil

from rest_framework import serializers

from .models import *
from .services import *

class IaResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IaResponse
        fields = '__all__'


class AudioListSerializer(serializers.Serializer):
    audio_responses = serializers.ListField(
        child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip_files(self, folder):
        shutil.make_archive(f'public/static/zip/{folder}', 'zip', f'public/static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        audio_responses = validated_data.pop('audio_responses')
        response_objs = []
        for audio_response in audio_responses:
            response_obj = IaResponse.objects.create(folder=folder, audio_response=audio_response)
            response_objs.append(response_obj)
            encode(audio_response)

        self.zip_files(folder.uid)
        return {'audio_responses': {}, 'folder': str(folder.uid)}
