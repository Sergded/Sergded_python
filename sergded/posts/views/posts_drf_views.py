from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from posts.models import Posts
from django.db.models import Count
from django.views import View
from .serializers_posts import PostsSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class Posts_APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class Posts_APIList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    pagination_class = Posts_APIListPagination

class Posts_APIUpdate(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class Posts_APIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class Posts_get(APIView):
    def get (self,request):
        p = Posts.objects.all()
        return Response({'posts':PostsSerializer(p, many=True).data})
    
    def post (self,request):
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'posts':serializer.data})
    
    def put (self,request,*args,**kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error":"Method PUT is not allowed"})
        
        try:
            instance = Posts.objects.get(pk=pk)
        except:
            return Response({"error":"Method PUT is not allowed"})
        
        serializer = PostsSerializer(data = request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})