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
