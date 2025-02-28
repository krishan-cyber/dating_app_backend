from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from Users.models import users

class swipetest(APITestCase):
    def test_swipe(self):
        url=reverse('swipe-user')
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        user2= users.objects.create(id=2, name="Test User2",number="78649893843",dateofbirth='2003-02-20',gender='F',orientation='s',intrests='reading')
        data={'swiped_id':2}
        response=client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_fetchprofiles(self):
        url=reverse('fetch_profiles')
        client=APIClient()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_matches(self):
        url=reverse('get-matches')
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)



