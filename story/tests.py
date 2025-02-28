from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from Users.models import users
from story.models import story
class story_check(APITestCase):
    def test_poststory(self):
        url=reverse('post_story')
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        data={'content':'everything working perfect'}
        response=client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_get_stories(self):
        url=reverse('get_story')
        client=APIClient()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_likestory(self):
        url=reverse('like_story',args=[1])
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        story.objects.create(user_id=user,content="hello doctor")
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


