from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Users.models import users as User
from .models import Swipe, Match
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from Users.serializers import usersSerializer
from datetime import date
from django.utils.timezone import now
from rest_framework import status

@api_view(["POST"])
def swipe_user(request):
    
    swiper_id = request.session.get("user_id")  
    swiped_id = request.data.get("swiped_id")  
    is_liked = request.data.get("is_liked", False)  

    if not swiper_id:
        return Response({"message": "User not authenticated"}, status=401)

    if not swiped_id:
        return Response({"message": "Swiped user ID is required"}, status=400)

    try:
        swiper = User.objects.get(id=swiper_id)
        swiped = User.objects.get(id=swiped_id)

        
        swipe, created = Swipe.objects.get_or_create(swiper=swiper, swiped=swiped, defaults={"is_liked": is_liked})

        if not created:  
            swipe.is_liked = is_liked
            swipe.save()

        
        if is_liked:
            if Swipe.objects.filter(swiper=swiped, swiped=swiper, is_liked=True).exists():
                
                Match.objects.create(user1=swiper, user2=swiped)
                return Response({"message": "It's a match!"}, status=200)

        return Response({"message": "Swipe recorded"}, status=200)

    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)


@api_view(["GET"])
def get_matches(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return Response({"message": "User not authenticated"}, status=401)

    try:
        user = User.objects.get(id=user_id)

        # Fetch unique matches
        matches = Match.objects.filter(Q(user1=user) | Q(user2=user)).distinct()

        # Use a set to track unique user IDs
        unique_matched_users = set()
        matched_users = []

        for match in matches:
            matched_user = match.user1 if match.user2 == user else match.user2

            if matched_user.id not in unique_matched_users:
                unique_matched_users.add(matched_user.id)  # Store ID to prevent duplicates
                matched_users.append({
                    "id": matched_user.id,
                    "name": matched_user.name,
                })

        return Response({"matches": matched_users}, status=200)

    except users.DoesNotExist:
        return Response({"message": "User not found"}, status=404)


@api_view(["GET"])
def fetch_profiles(request):
    min_age = int(request.GET.get("min_age", 18))
    max_age = int(request.GET.get("max_age", 100))
    genders = request.GET.getlist("gender")  

    
    current_year = now().year
    min_birth_year = current_year - max_age 
    max_birth_year = current_year - min_age  

    try:
        profiles = User.objects.filter(
            dateofbirth__year__gte=min_birth_year,  
            dateofbirth__year__lte=max_birth_year,  
            gender__in=genders,
            visibility=True 
        ).order_by("-verified") 
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    paginator = LimitOffsetPagination()
    paginated_profiles = paginator.paginate_queryset(profiles, request)

    if paginated_profiles is not None:
        serializer = usersSerializer(paginated_profiles, many=True)
        return paginator.get_paginated_response(serializer.data)

    
    serializer = usersSerializer(profiles, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)