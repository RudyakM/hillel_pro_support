from django.contrib import admin
from django.urls import path

from config.api import home

urlpatterns = [path("admin/", admin.site.urls), path("home/", home)]
