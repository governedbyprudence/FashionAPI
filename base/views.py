from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import fashion_serializer
from django.http import JsonResponse
import json
from .utils import apt_query
from .models import fashion
import random

@csrf_exempt
def api_view(request):
    if request.method == "GET":
        keys=request.GET
        message=""
        data={}
        serializer={}
        if len(keys)==0:
            data["random"]=1
            queryset,message=apt_query(data)
            serializer=fashion_serializer(queryset)
        else:
            for i in keys:
                if i=="place" or i=="accessories":
                    data[i]=request.GET.get(i).split(",")
                else:
                    data[i]=request.GET.get(i)
            queryset,message=apt_query(data)
            serializer=fashion_serializer(queryset,many=True)
        return JsonResponse({"message":message,"data":serializer.data},safe=False)
    elif request.method == "POST":
        print(json.loads(request.body))
        return JsonResponse({"message":"POST     request"})

