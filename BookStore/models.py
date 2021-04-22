from django.db import models

# Create your models here.
class UserInfo(models.Model):
	UserId = models.AutoField(primary_key=True)
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	UserName = models.CharField(max_length=50, unique = True)
	PassWord1 = models.CharField(max_length=50)
	PassWord2 = models.CharField(max_length=50)

	def __str__(self):
		return self.UserName