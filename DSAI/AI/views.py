from django.shortcuts import render
from django.http import HttpResponse
from .serializers import DataSerializer
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def main(request):
    print('good');
    return HttpResponse('good');

@api_view(['Get'])
def getTestData(request):
    datas = Post.objects.all()
    serializers = DataSerializer(datas, many=True)
    return Response(serializers.data);

def from_leo():
    return None