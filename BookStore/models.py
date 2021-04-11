from django.db import models

# Create your models here.
class UserInfo(models.Model):
	UserId = models.AutoField(primary_key=True)
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	UserName = models.CharField(max_length=50)
	PassWord = models.CharField(max_length=50)