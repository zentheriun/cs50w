from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'completed', 'priority', 
                 'due_date', 'completed_at', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'completed_at')