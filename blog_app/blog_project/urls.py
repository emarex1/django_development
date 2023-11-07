# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),#for login
    path("accounts/", include("accounts.urls")),#for signup
    path("", include("blog.urls")),
]