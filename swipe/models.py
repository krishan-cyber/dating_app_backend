from django.db import models
from django.db import models
from Users.models import users as User

class Swipe(models.Model):
    swiper = models.ForeignKey(User, on_delete=models.CASCADE, related_name="swiper")
    swiped = models.ForeignKey(User, on_delete=models.CASCADE, related_name="swiped")
    is_liked = models.BooleanField()  
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('swiper', 'swiped')  

class Match(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="match_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="match_user2")
    matched_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2') 

