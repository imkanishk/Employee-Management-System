from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50,null=True)
    doj = models.DateField(null=True)

    def __str__(self) -> str:
        return self.user.username

    
