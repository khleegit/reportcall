from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.index, name='index'),
    path('rp_daily_cs', views.rp_daily_cs, name='rp_daily_cs'),
    path('card_pm', views.card_pm, name='card_pm'),
    path('dash', views.dash, name='dash'),
]