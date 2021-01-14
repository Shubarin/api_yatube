from rest_framework import serializers

from .models import Comment, Post, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
