import shutil

from rest_framework import serializers

from .models import *
from .services import *


def zip_files(public_folder):
    shutil.make_archive(f'public/static/zip/{public_folder}', 'zip', f'public/static/{public_folder}')


class AudioSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False)
    public_folder = serializers.CharField(required=False)

    def create(self, validated_data):
        file = validated_data.pop('file')
        response_obj = Pdf.objects.create(file=file)
        encode(file)

        zip_files(response_obj.uid)
        return {'file': {}, 'public_folder': str(response_obj.uid)}
