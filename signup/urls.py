from django.contrib import admin
from django.urls import path,include
from .views import UserForm

app_name="signup"

urlpatterns = [
    path("",UserForm.as_view(),name="signup1")
]