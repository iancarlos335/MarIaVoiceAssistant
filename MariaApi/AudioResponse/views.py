from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AudioResponse.models import IaAudioResponse
from AudioResponse.serializers import IaAudioResponseSerializer


# Create your views here.
@csrf_exempt
def iaAudioResponseApi(request, id=0):
    if request.method == 'GET':
        iaAudioResponse = IaAudioResponse.objects.all()
        iaAudioResponse_serializer = IaAudioResponseSerializer(iaAudioResponse, many=True)
        return JsonResponse(iaAudioResponse_serializer.data, safe=False)

    elif request.method == 'POST':
        iaAudioResponse_data = JSONParser.parse(request)
        iaAudioResponse_serializer = IaAudioResponseSerializer(data=iaAudioResponse_data)
        if iaAudioResponse_serializer.is_valid():
            iaAudioResponse_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar.", safe=False)

    elif request.method == 'PUT':
        iaAudioResponse_data = JSONParser.parse(request)
        iaAudioResponse = IaAudioResponse.objects.get(id=iaAudioResponse_data['id'])
        iaAudioResponse_serializer = IaAudioResponseSerializer(iaAudioResponse, data=iaAudioResponse_data)
        if iaAudioResponse_serializer.is_valid():
            iaAudioResponse_serializer.save()
            return JsonResponse("Atualizado com sucesso!!", safe=False)
        return JsonResponse("Falha na atualização.", safe=False)

    elif request.method == 'DELETE':
        iaAudioResponse = IaAudioResponse.objects.get(id=id)
        iaAudioResponse.delete()
        return JsonResponse("Deletado com sucesso!", safe=False)
