from django.db import models

# Create your models here.
class UserRegister(models.Model):
    Name = models.CharField(max_length=30)
    User_Name = models.CharField(max_length=30)
    Pass_Word = models.CharField(max_length=30)
    Mobile_No = models.CharField(max_length=30)
    Mail_Id  = models.CharField(max_length=30)
    Locality = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    City  = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    
    def __str__(self) :
        return self.Name