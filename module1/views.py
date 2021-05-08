
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic,View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerListView,OwnerDetailView,OwnerCreateView
from .models import Advisor,Meetings
from django.contrib.auth.models import User

# Create your views here.

class ListView(View):
    def get(self,request):
        ctx = {"objects":Advisor.objects.all()}
        return render(request,"module1/list.html",ctx)


class HomeView(View):
    def get(self,request):

        return render(request,"module1/home.html")


class BookView(View,LoginRequiredMixin):
    def post(self,request,fk1,fk2):
        f1 = User.objects.filter(id=fk1)
        f2 = Advisor.objects.filter(id=fk2)
        meeting = Meetings(user=f1[0],advisor=f2[0])
        meeting.save()
        ctx={"object1":f1[0],"object2":f2[0]}
        return render(request,"module1/meeting_fixed.html",ctx)


class MeetingList(View,LoginRequiredMixin):
    def get(self,request,fk1):
        advisors = Meetings.objects.filter(user=fk1)

        objects = Advisor.objects.filter(id=advisors.advisor)
        ctx = {"objects":objects}
        return redirect("module1/list_meeting.html",ctx)


class MeetingList2(View,LoginRequiredMixin):

    def get(self,request,fk1):

        objects1 = Meetings.objects.filter(user=fk1)
        list1=[objects1[i].advisor.id for i in range(len(objects1))]
        objects = Advisor.objects.filter(id__in=list1)



        ctx = {"objects":objects}
        return render(request,"module1/list_meeting2.html",ctx)