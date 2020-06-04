from django.db import models
class task_user(models.Model):
    Id=models.AutoField(primary_key=True)
    F_name=models.CharField(max_length=50)
    L_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=40)
    gender=models.CharField(max_length=40,default='')
    country=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

    def __str__(self):
        return str(self.Id)
