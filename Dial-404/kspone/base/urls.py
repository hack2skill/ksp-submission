from django.urls import path
from . import views

urlpatterns =[
    
    path('login/login', views.loginpage, name="login"),
    path('help/', views.loginhelp, name="help"),
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('fingerprint/', views.fingerprint, name="fingerprint"),
    path('userguide/', views.userguide, name="userguide"),
    path("logout/", views.logoutuser, name = "logout"),
    path('pdf/', views.pdf, name="pdf"),
]