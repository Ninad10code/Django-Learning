from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),
    path('myfirstpage',views.myfirstpage,name="myfirstpage"),
    path('mysecondpage',views.mysecondpage,name="mysecondpage"),
    path('mythirdpage',views.mythirdpage,name="mythirdpage"),
    path('myimagepage',views.myimagepage,name="myimagepage"),
    path('myform',views.myform,name="myform"),
    path('submitform',views.submitform,name="submitform"),
    path('myform2',views.myform2,name="myform2"),

]