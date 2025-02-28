from rest_framework import serializers
from .models import story

class storySerializer(serializers.ModelSerializer):
    class Meta:
        model=story
        fields=['user_id','content','liked_by','created_at']
        