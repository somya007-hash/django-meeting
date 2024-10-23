from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.index),
    path("meeting-detail", views.meetup_detail)
]
