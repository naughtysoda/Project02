from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Board(models.Model):
    firstname = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    star = models.IntegerField(default=0,null=True)

    def __str__(self):
        return "{}-{}".format(self.firstname,self.star)

class Profile(models.Model):
    empid = models.CharField(max_length=15,primary_key=True,default='00000')
    name = models.CharField(max_length=30,default='ชื่อเล่น')
    position = models.CharField(max_length=20,default='ตำแหน่ง') #Position
    position_level = models.CharField(max_length=5,default='ระดับ') #LevelCode
    department_name = models.CharField(max_length=50,default='สังกัด') #DepartmentShort
    department_code = models.CharField(max_length=50,default='รหัสSAP') #NewOrganizationalCode
    workage = models.DateField(auto_now_add=False,null=True,default=timezone.now) #StaffDate - วันปัจจุบัน

class Star(models.Model):
    comment = models.TextField()
    point = models.IntegerField(null=True,default=0)
    yollow_card = models.IntegerField(null=True,default=0)
    date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=20,default='Progress')

class Staff(models.Model):
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    star = models.ForeignKey(Star,on_delete= models.CASCADE)