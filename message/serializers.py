from rest_framework import serializers
from .models import Message

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['sender_id','receiver_id','message']