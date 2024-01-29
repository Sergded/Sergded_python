from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from posts.models import Posts
from posts.views.custom_filters.posts_custom_filters import PostsFilterBackend
from django.db.models import Count
from django.views import View
from .serializers_posts import PostsSerializer
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import views
from rest_framework import viewsets


class Posts_APIfilter(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,PostsFilterBackend]
    search_fields = ['title', 'text']
    ordering_fields = ['title', 'counter']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostsSerializer
        return PostsSerializer

