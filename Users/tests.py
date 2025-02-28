from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from Users.models import users

class userTest(APITestCase):
    def test_sendOtp(self):
        url=reverse("send_otp")
        client=APIClient()
        data={"number":"6567898"}
        response=client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_createProfile(self):
        url=reverse("create-profile")
        client=APIClient()
        data={
    "number": "9876543209",
    "name": "anglina",
    "dateofbirth": "2000-05-15",
    "bio": "I love coding and hiking!",
    "gender": "M",
    "orientation": "s",
    "intrests": ["coding", "hiking"],
    "location": "New York"
}
        response=client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_deleteAccount(self):
        url=reverse("delete-account")
        client=APIClient()
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')  
        session = client.session
        session['user_id'] = user.id  
        session.save()
        response=client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_userDetail(self):
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')
        url=reverse("show-user-detail",args=['78649893840'])
        client=APIClient()
        response=client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_updateDetail(self):
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')
        url=reverse("update-user-detail",args=['78649893840'])
        client=APIClient()
        data={"name":"alfred noble"}
        response=client.patch(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_visibility(self):
        user = users.objects.create(id=1, name="Test User",number="78649893840",dateofbirth='2003-02-14',gender='M',orientation='s',intrests='reading')
        url=reverse("go-offline",args=['78649893840'])
        client=APIClient()
        data={"visibility":"false"}
        response=client.patch(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        



