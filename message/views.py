from django.shortcuts import render
from rest_framework.views import APIView
from .models import Message
from swipe.models import Match
from rest_framework.response import Response
from rest_framework import status
from .serializers import messageSerializer
from Users.models import users
from Users.serializers import usersSerializer
from collections import defaultdict

class message_handle(APIView):
    def post(self,request):
        data=request.data
        serializer=messageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        sender_id=request.session.get("user_id") 
        receiver_id=serializer.data.get("receiver_id")
        message=serializer.data.get("message")
        try:
            sender=users.objects.get(id=sender_id)
            receiver=users.objects.get(id=receiver_id)
        except:
            return Response({"message":"user doesnot exist"},status=status.HTTP_404_NOT_FOUND)
        try:
            match=Match.objects.filter(user1=sender,user2=receiver)|Match.objects.filter(user1=receiver,user2=sender)

        except:
            return Response({"message":"you cant send message without macthing"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        message_send=Message.objects.create(sender_id=sender,receiver_id=receiver,message=message)
        return Response(status=status.HTTP_200_OK)

    def get(self,request,pk):
        try:
            receiver=pk
            sender = users.objects.get(id=request.session.get("user_id"))
            messages = Message.objects.filter(sender_id=sender.id,receiver_id=pk).order_by("created_at")

            if not messages.exists():
                return Response({"message": "No messages found for this user"}, status=status.HTTP_200_OK)

            grouped_messages = defaultdict(list)

            for message in messages:
                grouped_messages[message.receiver_id.id].append(message.message)  

            response_data = []
            for receiver_id, messages_list in grouped_messages.items():
                response_data.append({
                    "sender_id": sender.id,  
                    "receiver_id": receiver_id, 
                    "messages": messages_list 
                })

            return Response(response_data, status=status.HTTP_200_OK)

        except users.DoesNotExist:
            return Response({"error": "Sender not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  



class message_user(APIView):
    def get(self, request):
        try:
            sender = users.objects.get(id=request.session.get("user_id"))  
            messages = Message.objects.filter(sender_id=sender.id).order_by("created_at") 

            if not messages.exists():
                return Response({"message": "No messages found for this user"}, status=status.HTTP_200_OK)

            grouped_messages = defaultdict(list)

            for message in messages:
                grouped_messages[message.receiver_id.id].append(message.message)  

            response_data = []
            for receiver_id, messages_list in grouped_messages.items():
                response_data.append({
                    "sender_id": sender.id,  
                    "receiver_id": receiver_id, 
                    "messages": messages_list  
                })

            return Response(response_data, status=status.HTTP_200_OK)

        except users.DoesNotExist:
            return Response({"error": "Sender not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
