from django.shortcuts import render

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

class EntryVewSet(object):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer