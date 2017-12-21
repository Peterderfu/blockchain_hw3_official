import os, json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.serializers import ApiSerializer

module_dir = os.path.dirname(__file__)

@csrf_exempt
def getConfig(request):
  if request.method == 'GET':
    data = json.load(open(os.path.join(module_dir, 'static/config.json')))
    return JsonResponse(data)
  else:
    return JsonResponse({}, status=400)

@csrf_exempt
def getHistory(request):
  if request.method == 'GET':
    data = json.load(open(os.path.join(module_dir, 'static/history.json')))
    return JsonResponse(data)
  else:
    return JsonResponse({}, status=400)

@csrf_exempt
def getSymbols(request):
  if request.method == 'GET':
    data = json.load(open(os.path.join(module_dir, 'static/symbols.json')))
    return JsonResponse(data)
  else:
    return JsonResponse({}, status=400)
