# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.db.models import Q


# Create your views here.



def loginb(req):
    if req.method == "GET":
        return render_to_response('loginb.html')
    if req.method == "POST":
        pass



def index(req):
    if req.method == "GET":
        return render_to_response('index.html')
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