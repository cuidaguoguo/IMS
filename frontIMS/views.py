# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.db.models import Q


# Create your views here.


def index(req):
    if req.method == "GET":
        return render_to_response('login.html')
    if req.method == "POST":
        pass