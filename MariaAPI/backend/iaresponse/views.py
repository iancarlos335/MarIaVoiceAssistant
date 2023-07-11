from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class GetIaResponseData(APIView):
    parser_classes = [FileUploadParser]
    serializer_class = serializers.IaResponseSerializer

    def get(self, request, id, *args, **kwargs):
        iaResponse = models.IaResponse.objects.get(id=id)
        return FileResponse(iaResponse.audio_file.open())

    @api_view(["POST"])
    def post(self, request, filename, format=None):
        data = request.data[filename]

        # ...
        # do some stuff with uploaded file
        # ...

        serializer = serializers.IaResponseSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            data = serializer.data
            return Response(data)
