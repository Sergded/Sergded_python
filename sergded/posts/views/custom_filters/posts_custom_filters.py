from rest_framework import filters
from django.db.models.query import QuerySet
from posts.models import models
from posts.models import Posts
from django.views import View

class PostsFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset:QuerySet[Posts], view):
        max_counter = request.query_params.get('max_counter')
        if max_counter:
            return queryset.filter(counter__lte=max_counter)
        return queryset