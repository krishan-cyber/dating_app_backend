from django.db import models
from Users.models import users as User

class story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    content=models.CharField(max_length=1000,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name="liked_stories", blank=True)

