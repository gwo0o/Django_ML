from django.shortcuts import redirect
from django.http import HttpResponse
from .serializers import DataSerializer
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
import json

# Create your views here.

def main(request):
    print('good');
    return HttpResponse('good');

@api_view(['Get'])
def getTestData(request):
    datas = Post.objects.all()
    serializers = DataSerializer(datas, many=True)
    return Response(serializers.data);

@api_view(['POST'])
def setTestData(request):
    if request.method == 'GET':
        print('GET_WORK')
    if request.method =='POST':
        print('SET_WORK')
    post = Post()
    data = str(request.data).replace('\'', '\"')
    data = json.loads(data)
    post.post_group = data['post_group']
    post.post_title = data['post_title']
    post.post_content = data['post_content']
    post.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    post.save()
    return redirect('getTestData')

@api_view(['POST'])
def updateTestData(request):
    if request.method == 'GET':
        print('GET_WORK')
    if request.method =='POST':
        print('SET_WORK')
    data = str(request.data).replace('\'', '\"')
    data = json.loads(data)
    target_id = data['target_id']
    post = Post.objects.get(field_id = target_id)
    data = data['changes']
    for key in data.keys():
        if key == 'post_group':
            post.post_group = data['post_group']
        elif key == 'post_title':
            post.post_title = data['post_title']
        elif key == 'post_content':
            post.post_content = data['post_content']
    post.save()
    return redirect('getTestData')

@api_view(['POST'])
def deleteTestData(request):
    if request.method == 'GET':
        print('GET_WORK')
    if request.method =='POST':
        print('SET_WORK')
    data = str(request.data).replace('\'', '\"')
    data = json.loads(data)
    target_id = data['target_id']
    post = Post.objects.get(field_id = target_id)
    post.delete()
    return redirect('getTestData')