from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from Users.models import users
class message_check(TestCase):
    def test_sendMessage(self):
        url=reverse('send_message')
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        data={"receiver_id":1,"message":"hello world"}
        response=client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_receiveMessage(self):
        client=APIClient()
        url=reverse("load_chats",args=[1])
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_all_messages(self):
        client=APIClient()
        url=reverse("all-chats")
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        


