from django.contrib import admin
from django.urls import path

from config.api.exchange_rates import btc_usd, history, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("btc_usd/", btc_usd),
    path("history/", history),
]
