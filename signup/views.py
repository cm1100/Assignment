from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

class UserForm(View):

    def post(self,request):

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("done")
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect(reverse_lazy("module1:home"))
        else:
            ctx={"form":form}
            return redirect(reverse_lazy("signup:signup1"),ctx)


    def get(self,request):
        form = SignUpForm()
        return render(request,'signup/signup.html',{"form":form})



