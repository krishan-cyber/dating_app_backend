from django.db import models
from Users.models import users
class Message(models.Model):
    sender_id=models.ForeignKey(users,on_delete=models.CASCADE,related_name='sender')
    receiver_id=models.ForeignKey(users,on_delete=models.CASCADE,related_name='receiver')
    message=models.CharField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

