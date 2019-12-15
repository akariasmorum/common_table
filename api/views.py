from django.shortcuts import render
from table.models import unblockings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        all_rows = list(unblockings.objects.values())
        return JsonResponse(all_rows, safe=False)

    elif request.method == 'POST':
        js = json.loads(request.body)
        print(js)
