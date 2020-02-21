from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('sex', views.male,name='male'),
    # path('sex/male/1', views.male_region_1.as_view(),name='male_1'),
    # path('sex/male/3', views.male_region_3.as_view(),name='male_3'),
    
    
]