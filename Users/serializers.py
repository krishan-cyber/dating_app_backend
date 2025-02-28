from rest_framework import serializers
from .models import users

class usersSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()
    orientation_display = serializers.SerializerMethodField()
    interests_display = serializers.SerializerMethodField()
    intrests = serializers.ListField(child=serializers.ChoiceField(choices=[i[0] for i in users.intrests_choices]))

    class Meta:
        model = users
        fields = [
            'number', 'name', 'dateofbirth', 'bio', 'verified', 'gender', 'gender_display',
            'visibility', 'orientation', 'orientation_display', 'intrests', 'interests_display', 'location', 'profile_pic'
        ]

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_orientation_display(self, obj):
        return obj.get_orientation_display()

    def get_interests_display(self, obj):
        return [dict(users.intrests_choices).get(i, i) for i in obj.intrests]
class visibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=['visibility']
