from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('mysecondpage',views.mysecondpage,name='mysecondpage')
]