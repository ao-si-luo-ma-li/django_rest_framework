from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# 定义 ViewSet
import django_filters
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer

# queryset设置为Model的queryset，serializer_class设置为刚才定义的serializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryVewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

# 使用queryset和serializer_class代替model变量, 使我们能更加好的控制API行为, 这也是我们推荐的使用方式


@api_view(['POST', 'GET'])
def add_blog(request, *args):

	#1、接收request数据
	if request.method == 'GET':
		for j in request.query_params:
			dict[j] = request.query_params[j]
		return dict
	elif request.method == 'POST':
		for j in request.data:
			dict[j] = request.data[j]
		return dict
	# return Response()
	# 2、处理数据
	# 2-1、首先要判断get或post过来的数据是否满足我们的要求，例如缺少字段、类型错误等。

	# 3、返回结果

@api_view(['POST', 'GET'])
def add_user(request, *args):
	p2 = User(name="yb", mail="456@qq.com")
	p2.save()
	user_list = User.objects.all()
	return HttpResponse(user_list)