from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.index, name='index'),
    path('ls_period_cs', views.ls_period_cs, name='ls_period_cs'),
    path('card_pm', views.card_pm, name='card_pm'),
    path('dash', views.dash, name='dash'),
]