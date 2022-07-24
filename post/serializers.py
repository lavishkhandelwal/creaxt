from tkinter.tix import Tree
from rest_framework import serializers
from .models import post
from comment.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = post
        fields = ('title', 'content', 'created_at', 'updated_at', 'topic', 'user', 'comment')