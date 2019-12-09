from django.urls import path
from . import views
from django.conf.urls import url
from .views import mainpage,offense,defense
urlpatterns=[
        path('NFL/',views.mainpage),
        path('NFL/offense/',views.offense,name='offense'),
        path('NFL/defense/',views.defense,name='defense'),
        ]
