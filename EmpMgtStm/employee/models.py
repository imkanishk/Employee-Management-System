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
    
class EmployeeEducation(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pg = models.CharField(max_length=50, null=True)
    yop_pg = models.CharField(max_length=50, null=True)
    ug = models.CharField(max_length=50, null=True)
    yop_ug = models.CharField(max_length=50, null=True)
    class_XII = models.CharField(max_length=50, null=True)
    yop_class_XII = models.CharField(max_length=50, null=True)
    class_X = models.CharField(max_length=50, null=True)
    yop_class_X = models.CharField(max_length=50, null=True)
      
    gender = models.CharField(max_length=50,null=True)
    doj = models.DateField(null=True)

    def __str__(self) -> str:
        return self.user.username
    
class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company1_name = models.CharField(max_length=50, null=True)
    company1_desig = models.CharField(max_length=50, null=True)
    company1_duration = models.CharField(max_length=50, null=True)
    company2_name = models.CharField(max_length=50, null=True)
    company2_desig = models.CharField(max_length=50, null=True)
    company2_duration = models.CharField(max_length=50, null=True)
    company3_name = models.CharField(max_length=50, null=True)
    company3_desig = models.CharField(max_length=50, null=True)
    company3_duration = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.user.username 

    
 