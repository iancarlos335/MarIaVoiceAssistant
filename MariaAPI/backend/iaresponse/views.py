from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class IaVoiceResponse(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = AudioListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'status': '200',
                     'message': 'Arquivos de audio enviados com sucesso',
                     'data': serializer.data})

            return Response({
                'status': 400,
                'message': 'Alguma coisa deu errado',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)

        # class GetIaResponseData(APIView):
#    parser_classes = [FileUploadParser]
#    serializer_class = serializers.IaResponseSerializer
#
#    def get(self, request, id, *args, **kwargs):
#        iaResponse = models.IaResponse.objects.get(id=id)
#        return FileResponse(iaResponse.audio_file.open())
#
#    @api_view(["POST"])
#    def post(self, request, filename, format=None):
#        data = request.data[filename]
#
#        # ...
#        # do some stuff with uploaded file
#        # ...
#
#        serializer = serializers.IaResponseSerializer(data=request.data)
#        if serializer.is_valid():
#            print(serializer.data)
#            data = serializer.data
#            return Response(data)
#
