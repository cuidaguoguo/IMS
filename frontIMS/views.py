# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from _mysql import result
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import uuid
import re, base64
from django.utils.html import escapejs

from frontIMS import models

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.db.models import Q
import json
import time
import time
from frontIMS.models import Institude, Teacher, Couser, Major, Grade, Student, Score

# Create your views here.


@csrf_exempt
def loginb(req):
    if req.method == "GET":
        return render_to_response('loginb.html')
    if req.method == "POST":
        try:
            account = req.POST['account']
            password = req.POST['password']
        except Exception as e:
            result = {
                'status': 0,
                'message': "获取信息失败"
            }
            return HttpResponse(json.dumps(result))
        else:
            if models.Teacher.objects.filter(Q(TeacherId=account)):
                user = models.Teacher.objects.get(TeacherId=account)
                if user.PassWord == password:
                    result = {
                        'status': 1,
                        'message': "登录成功",
                        'username':user.UserName,
                        'teacherid':user.TeacherId
                    }

                    return HttpResponse(json.dumps(result))
                elif user.PassWord != password:
                    result = {
                        'status': 0,
                        'message': "用户密码不正确",
                    }
                    return HttpResponse(json.dumps(result))
            else:
                result = {
                    'status': 0,
                    'message': "用户密码不正确",
                }
                return HttpResponse(json.dumps(result))
            


@csrf_exempt
def index(req):
    if req.method == "GET":
        teacherid = req.COOKIES.get('teacherid')
        username = req.COOKIES.get('username')
        teacher = models.Teacher.objects.all()
        return render_to_response('index.html',{"teacher":teacher})
    if req.method == "POST":
        pass


def teacherguanli(req):
    if req.method == "GET":
        return render_to_response('teacherguanli.html')
    if req.method == "POST":
        pass


def studentguanli(req):
    if req.method == "GET":
        return render_to_response('studentguanli.html')
    if req.method == "POST":
        pass