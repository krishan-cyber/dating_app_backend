from django.db import models
from django.utils.timezone import now, timedelta
from multiselectfield import  MultiSelectField
def get_expiry_time():
    return now() + timedelta(minutes=10)

class otp(models.Model):
    number=models.CharField(unique=True,max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    otp_digits=models.CharField(max_length=6)
    expires_at=models.DateTimeField(default=get_expiry_time())


class users(models.Model):
    id = models.AutoField(primary_key=True)
    Gender_choices=(('M','Male'),('F','Female'),('O','other'))
    orientation_choices=(('s','straight'),('h','homosexual'),('p','pansexual'),('b','bisexual'))
    intrests_choices=(('reading','Reading'),('hiking','Hiking'),('coding','Coding'),('dancing','Dancing'))
    number=models.CharField(unique=True,max_length=15)
    name=models.CharField(max_length=20)
    dateofbirth=models.DateField()
    bio=models.CharField(max_length=50)
    verified=models.BooleanField(default=False)
    gender=models.CharField(choices=Gender_choices,null=False)
    visibility=models.BooleanField(default=True)
    orientation=models.CharField(choices=orientation_choices,null=False)
    intrests=MultiSelectField(choices=intrests_choices,null=False)
    location=models.CharField(max_length=255)
    profile_pic=models.ImageField(upload_to='profile_pics/',null=True)
    def __str__(self):
        return self.name




