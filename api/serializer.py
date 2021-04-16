
from django.core.files.base import ContentFile
from rest_framework import serializers

from api.models import UserApp, Project, Task


class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'