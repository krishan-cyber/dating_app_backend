from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .models import otp, users
from django.utils.timezone import now, timedelta
from .serializers import usersSerializer, visibilitySerializer
from rest_framework import generics
from rest_framework import status

@api_view(["POST"])
def send_otp(request):
    
    number = request.data.get("number")

    if not number:
        return Response({"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

    otp_num = str(random.randint(100000, 999999))

   
    otp_instance, created = otp.objects.get_or_create(number=number)

    
    otp_instance.otp_digits = otp_num
    otp_instance.expires_at = now() + timedelta(minutes=10)
    otp_instance.save()
    
    return Response({"message": f"OTP sent successfully"},status=status.HTTP_200_OK)

@api_view(["POST"])
def verify_otp(request):
   
    number = request.data.get("number")
    otp_user = request.data.get("otp")

    if not number or not otp_user:
        return Response({"message": "Phone number and OTP are required"}, status=400)

    try:
        otp_instance = otp.objects.get(number=number)

       
        if otp_instance.expires_at and otp_instance.expires_at < now():
            return Response({"message": "OTP expired"}, status=400)

        
        if otp_instance.otp_digits == otp_user:
            
            try:
                user = users.objects.get(number=number)
                request.session["user_id"] = user.id  
                return Response({"message": "OTP verified. User logged in"}, status=200)

            except users.DoesNotExist:
                return Response({"message": "OTP verified. User needs to sign up"}, status=201)

            return Response({"message": "OTP verified", "user_id": user.id}, status=200)
        else:
            return Response({"message": "Invalid OTP"}, status=400)

    except otp.DoesNotExist:
        return Response({"message": "OTP not found"}, status=404)

class CreateUserProfileView(generics.CreateAPIView):
   
    queryset = users.objects.all()
    serializer_class = usersSerializer
    def perform_create(self, serializer):
        user = serializer.save() 
        self.request.session["user_id"] = user.id 

class ShowUserDetails(generics.RetrieveAPIView):
    
    queryset = users.objects.all()
    serializer_class = usersSerializer
    lookup_field = "number"

class UpdateUserDetails(generics.UpdateAPIView):
    
    queryset = users.objects.all()
    serializer_class = usersSerializer
    lookup_field = "number"

class UserGoOffline(generics.UpdateAPIView):
    
    queryset = users.objects.all()
    serializer_class = visibilitySerializer
    lookup_field = "number"

@api_view(["DELETE"])
def delete_account(request):
    
    user_id = request.session.get("user_id")  

    if not user_id:
        return Response({"message": "User not authenticated"}, status=401)

    try:
        user = users.objects.get(id=user_id)
        user.delete()
        return Response({"message": "Account deleted successfully"}, status=200)
    except users.DoesNotExist:
        return Response({"message": "User not found"}, status=404)
