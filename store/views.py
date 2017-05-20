from django.http import HttpResponse

from .models import User
from .models import Post
from .models import Group
from .models import Acadamic_Record
from django.http import Http404, request

from store.serializers import UserSerializer
from store.serializers import PostSerializer
from store.serializers import GroupSerializer
from store.serializers import Acadamic_RecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import requests
#import os
class UserList(APIView):
    #def index(request):
        #times = int(os.environ.get('TIMES', 3))
        #return HttpResponse('Hello! ' * times)
    def get(self, request):
        users = User.objects.all()
        #serializer_class = UserSerializer
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    def delete(self, request, u_id, format=None):
        user = self.get_object(pk =u_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''
class PostList(APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    def delete(self, request, post_id, format=None):
        post = self.get_object(pk = post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''
class GroupList(APIView):

    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    def delete(self, request, g_id, format=None):
        group = self.get_object(pk = g_id)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''
class Acadamic_RecordList(APIView):

    def get(self, request, format=None):
        acadamic_records = Acadamic_Record.objects.all()
        serializer = Acadamic_RecordSerializer(acadamic_records, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Acadamic_RecordSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
    def delete(self, request, a_id, format=None):
        acadamic_record = self.get_object(pk = a_id)
        acadamic_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''















#from django.http import HttpResponse
#from django.template import loader

#from .models import *

#def post(request):
 #   template = loader.get_template('post.html')
  #  context = {
   #     #'posts': Post.objects.all(),
    #}
    #return HttpResponse(template.render(context ,request))

#def user(request):
 #   template = loader.get_template('user.html')
  #  context = {

#    }
 #   return HttpResponse(template.render(context ,request))

#def group(request):
 #   template = loader.get_template('group.html')
  #  context = {

   # }
    #return HttpResponse(template.render(context ,request))

#def acadamic_record(request):
 #   template = loader.get_template('acadamic_record.html')
  #  context = {

   # }
    #return HttpResponse(template.render(context ,request))%#


















'''
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''