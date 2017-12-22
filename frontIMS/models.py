# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Admin(models.Model):
    '''
    管理员表， 用作后台管理
    '''
    Id = models.AutoField(primary_key=True)
    Account = models.CharField(null=False, blank=False, unique=True, max_length=25)
    Password = models.CharField(null=False, blank=False, max_length=25)
    DateTime = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    '''
    1.身份标识
        0学生
        1教师
    2.性别标识
        0男生
        1女生
    '''
    Id = models.AutoField(primary_key=True)
    Identity = models.PositiveSmallIntegerField(default=0, null=False)
    PassWord = models.CharField(max_length=20, null=False)
    Sex = models.PositiveSmallIntegerField(default=0, null=False)
    UserName = models.CharField(max_length=10, null=False)
    Institude = models.CharField(null=True, max_length=20)




class Student(models.Model):
    '''
    学生表
    '''
    Id = models.AutoField(primary_key=True)
    Grade = models.CharField(null=False, max_length=20)
    Major = models.CharField(null=True, max_length=20)



class Teacher(models.Model):
    '''
    教师表
    '''
    Id = models.AutoField(primary_key=True)
    cNO = models.CharField(null=False, max_length=20)



class Score(models.Model):
    '''
    成绩表
    '''
    Id = models.AutoField(primary_key=True)
    Score = models.CharField(null=False, max_length=20)
    cNO = models.CharField(null=False, max_length=20)


class Couser(models.Model):
    '''
    课程表
    '''

    cNO = models.CharField(primary_key=True, max_length=20)
    CouserName = models.CharField(null=True, max_length=20)
    Credit = models.CharField(null=True, max_length=20)
    Period = models.CharField(null=False, max_length=20 )
    
