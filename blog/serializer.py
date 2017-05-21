# coding:utf-8
# 生成REST API最少需要定义下面3个。 
# - Serializer 
# - ViewSet 
# - URL pattern 
# Serializer是将「Model序列化」，ViewSet是API的应答器，URL Pattern定义了URL的路由

from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = User
		fields = ('name', 'mail')	
			
class EntrySerializer(serializers.ModelSerializer):
	class Meta(object):
		model = User
		fields = ('title', 'body', 'created_at', 'status', 'author')
		
# 需要继承serializers.ModelSerializer， fields为API想要得到的字段