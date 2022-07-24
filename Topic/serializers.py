from rest_framework import serializers
from .models import topic
from django.contrib.auth.models import User
from post.serializers import PostSerializer

class TopicSerializer(serializers.ModelSerializer):
    post = PostSerializer(many = True, read_only = True)
    class Meta:
        model = topic
        fields = ('name', 'title', 'author',
                  'description', 'slug', 'created_at', 'updated_at', 'post')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        