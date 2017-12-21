from django.conf.urls import url, include
from frontIMS import views as views


urlpatterns =[
    url(r'loginb$', views.loginb),
    url(r'index$', views.index),
    url(r'teacherguanli$', views.teacherguanli),
    url(r'studentguanli$', views.studentguanli),
]