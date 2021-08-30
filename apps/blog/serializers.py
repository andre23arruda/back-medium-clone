from rest_framework import serializers
from .models import BlogPage


class BlogPageSerializer(serializers.ModelSerializer):
    '''BlogPage Serializer'''
    class Meta:
        model = BlogPage
        fields = '__all__'
