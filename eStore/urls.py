"""learnSQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("tickets/", views.tickets, name="tickets"),
    path("addcustomer/", views.addcustomer, name="addcustomer"),
    path("<int:ticketID>", views.ticketdetails, name="ticketdetails"),
    path("searchticket", views.searchticket, name="searchticket"),
    path("maketicket/", views.maketicket, name="maketicket"),
    path("searchcustomer/", views.searchcustomer, name="searchcustomer"),
    path("about/", views.about, name="about"),
    path("addstatus/", views.addstatus, name="addstatus"),
    path("addfault/", views.addfault, name="addfault"),
    path("adddata/", views.adddata, name="adddata"),
    path("loginview/", views.loginview, name="loginview"),
    path("logoutview/", views.logoutview, name="logoutview"),
    path("changestatus/", views.changestatus, name="changestatus")
]
