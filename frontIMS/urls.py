from django.conf.urls import url, include
from frontIMS import views as views


urlpatterns =[
    url('r^index$',views.index),
]