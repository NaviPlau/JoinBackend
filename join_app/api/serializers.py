from rest_framework import serializers
from join_app.models import Contact, Task
from django.contrib.auth import get_user_model
from join_auth.api.serializers import UserProfileSerializer
from join_auth.models import UserProfile
User = get_user_model()

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'fullname', 'phone', 'email', 'initials', 'initialsColor', 'user']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    

class SubtaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    assignedTo = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserProfile.objects.all()
    )  

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'dueDate',
            'subtasks',
            'priority',
            'category',
            'column',
            'assignedTo',
        ]

    def create(self, validated_data):
        """
        Handle IDs for the assignedTo field during task creation.
        """
        assigned_profiles = validated_data.pop('assignedTo', [])
        task = super().create(validated_data)  
        task.assignedTo.set(assigned_profiles) 
        return task

    def update(self, instance, validated_data):
        """
        Handle IDs for the assignedTo field during task updates.
        """
        assigned_profiles = validated_data.pop('assignedTo', [])
        instance = super().update(instance, validated_data)  
        instance.assignedTo.set(assigned_profiles)
        return instance
    
    

    