from django.urls import path

from . import views

urlpatterns = [
    path('checkUrl', views.checkUrl, name='checkUrl'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('report_pdf', views.report_pdf, name='report_pdf')
    
]