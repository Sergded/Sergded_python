from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from posts.models import Posts
from django.db.models import Count
from django.views import View

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.description = validated_data.get('description', instance.description)
        instance.counter = validated_data.get('counter', instance.counter)
        instance.Int_field = validated_data.get('Int_field', instance.Int_field)    
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance