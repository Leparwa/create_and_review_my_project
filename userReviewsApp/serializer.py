from django.contrib.auth import models
from rest_framework import serializers
from .models import Project, Review

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_image', 'title', 'description', 'link','owner',)
        read_only_fields = ('project_image',)