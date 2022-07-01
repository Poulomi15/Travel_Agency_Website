from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index,name = "home"),
    path("about",views.about,name = "about"),
    path("services",views.services,name = "services"),
    path("aroundcity",views.aroundcity,name = "aroundcity"),
    path("aroundstate",views.aroundstate,name = "aroundstate"),
    path("aroundcountry",views.aroundcountry,name = "aroundcountry"),
    path("aroundcontinent",views.aroundcontinent,name = "aroundcontinent"),
    path("contact",views.contact,name = "contact"),

]