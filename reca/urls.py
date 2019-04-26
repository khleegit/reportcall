from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.index, name='index'),
    path('rp_period_user', views.rp_period_user, name='rp_period_user'),
    path('ls_period_cs', views.ls_period_cs, name='ls_period_cs'),
    path('ls_period_csct', views.ls_period_csct, name='ls_period_csct'),
    path('card_pm', views.card_pm, name='card_pm'),
    path('dash', views.dash, name='dash'),
]