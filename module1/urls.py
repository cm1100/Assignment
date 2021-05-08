from django.contrib import admin
from django.urls import path,include
from .views import HomeView,ListView,BookView,MeetingList,MeetingList2


app_name="module1"

urlpatterns = [

    path("",HomeView.as_view(),name="home"),
    path("list",ListView.as_view(),name="list"),
    path("book_meating/<int:fk1>/<int:fk2>",BookView.as_view(),name="book_meeting"),
    path("meetings_list/<int:fk1>/<int:fk2>",MeetingList.as_view(),name="meeting_list"),
    path("meetings_list2/<int:fk1>",MeetingList2.as_view(),name="meeting_list2")
]
