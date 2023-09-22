from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class regmodel(models.Model):
    nm=models.CharField(max_length=20)
    eml=models.EmailField()
    num=models.CharField(max_length=20)
    bd=models.CharField(max_length=20)
    edct=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class profile1(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Companyprofile1(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

w=[('Online','Online'),('Offline','Offline'),('hybrid','hybrid')]
e=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('>5','>5')]
j=[('part time','part time'),('Full time','Full time')]
class postjobmodel1(models.Model):
    cnm=models.CharField(max_length=20)
    eml=models.EmailField()
    ttl=models.CharField(max_length=20)
    wktp=models.CharField(max_length=20,choices=w)
    ex=models.CharField(max_length=20,choices=e)
    jbtp=models.CharField(max_length=20,choices=j)

ex=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('>5','>5')]
class applyjobmodel1(models.Model):
    cn=models.CharField(max_length=20)
    dsg=models.CharField(max_length=20)
    nm=models.CharField(max_length=20)
    eml=models.EmailField()
    qlfn=models.CharField(max_length=20)
    phno=models.CharField(max_length=20)
    ex=models.CharField(max_length=20,choices=ex)
    cv=models.ImageField(upload_to="jobportalapp/static")
    