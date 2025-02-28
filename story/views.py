from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import storySerializer
from .models import story
from rest_framework.response import Response
from rest_framework import status
from Users.models import users
from rest_framework.pagination import LimitOffsetPagination

class stories(APIView):
    def post(self,request):
        try:
            user_id=request.session.get("user_id")
            serializer=storySerializer(data=request.data)
            user=users.objects.get(id=user_id)
            if serializer.is_valid():
                serializer.save()
            content=serializer.data['content']
            storyObj=story.objects.create(user_id=user,content=content)
        except:
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message":"story uploaded successfully"},status=status.HTTP_200_OK)

    def get(self, request):
        limit = int(request.GET.get("limit", 10))
        offset = int(request.GET.get("offset", 0))  
        
        stories = story.objects.order_by("-created_at")[offset : offset + limit] 

        serializer = storySerializer(stories, many=True)
        return Response({
            "count": story.objects.count(), 
            "limit": limit,
            "offset": offset,
            "results": serializer.data
        }, status=status.HTTP_200_OK)

class like_story(APIView):
    def get(self,request,story_id):
        try:
            story1=story.objects.get(id=story_id)
        except:
            return Response({"message":"story doesnt exist"},status=status.HTTP_404_NOT_FOUND)
        try:
            user=users.objects.get(id=request.session.get('user_id'))
            story1.liked_by.add(user)
            story1.save()
        except Exception as e:
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer=storySerializer(story1)
        return Response({"message":"story liked","story":serializer.data},status=status.HTTP_200_OK)