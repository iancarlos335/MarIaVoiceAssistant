import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    #data['headers'] = request.headers
    data['content_type'] = request.content_type
    #data['headers'] = dict(request.headers)
    return JsonResponse(data)