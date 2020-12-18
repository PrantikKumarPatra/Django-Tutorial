from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('mysecondpage',views.mysecondpage,name='mysecondpage'),
    path('mythirdpage',views.mythirdpage,name='mythirdpage'),
    path('myimagepage',views.myimagepage,name='myimgaepage'),
    path('myimagepage2',views.myimagepage2,name='myimagepage2'),
    path('myform',views.myform,name='myform'),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('myform2',views.myform2,name='myform2')
]