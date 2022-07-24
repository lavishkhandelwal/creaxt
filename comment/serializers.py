from rest_framework import serializers
from .models import comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('title', 'content', 'created_at', 'updated_at', 'post', 'user')