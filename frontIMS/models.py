# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Institude(models.Model):
    '''
    学院表
    '''
    InstitudeId = models.CharField(primary_key=True, max_length=20)
    InstitudeName = models.CharField(null=False, max_length=20)

    def __unicode__(self):
        return self.InstitudeName


class Teacher(models.Model):
    '''
    教师表
    '''
    TeacherId = models.CharField(primary_key=True, max_length=20)
    PassWord = models.CharField(max_length=20, null=False)
    UserName = models.CharField(max_length=10, null=False)
    InstitudeId = models.ForeignKey(Institude, max_length=20)

    def __unicode__(self):
        return self.UserName



class Couser(models.Model):
    '''
    课程表
    '''

    CouserId = models.CharField(primary_key=True, max_length=20)
    CouserName = models.CharField(null=False, max_length=20)
    Period = models.CharField(null=False, max_length=20 )
    TeacherId = models.ForeignKey(Teacher, max_length=20)

    def __unicode__(self):
        return self.CouserName



class Major (models.Model):
    '''
    专业表
    '''
    MajorId = models.CharField(primary_key=True, max_length=20)
    MajorName = models.CharField(null=False, max_length=20)
    InstitudeId = models.ForeignKey(Institude, max_length=20)

    def __unicode__(self):
        return self.MajorName


class Grade (models.Model):
    '''
    班级表
    '''
    GradeId = models.CharField(primary_key=True, max_length=20)
    GradeName = models.CharField(null=False, max_length=20)
    GradeNum = models.CharField(null=False, max_length=20)
    MajorId = models.ForeignKey(Major, max_length=20)
    InstitudeId = models.ForeignKey(Institude, max_length=20)

    def __unicode__(self):
        return self.GradeName


class Student(models.Model):
    '''
    学生表
    '''
    StudentId = models.CharField(primary_key=True, max_length=20)
    PassWord = models.CharField(max_length=20, null=False)
    UserName = models.CharField(max_length=10, null=False)
    StuTeacher = models.ManyToManyField(Couser)
    GradeId = models.ForeignKey(Grade, max_length=20)
    MajorId = models.ForeignKey(Major, max_length=20)
    InstitudeId = models.ForeignKey(Institude, max_length=20)

    def __unicode__(self):
        return self.StudentId

class Score(models.Model):
    '''
    成绩表
    '''
    ScoreId = models.CharField(primary_key=True, max_length=20)
    Score = models.CharField(null=False, max_length=20)
    CouserId = models.ForeignKey(Couser, max_length=20)
    StudentId = models.ForeignKey(Student, max_length=20)

    def __unicode__(self):
        return self.ScoreId

