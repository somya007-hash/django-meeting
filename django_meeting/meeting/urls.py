from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.index, name= "all-mettups"),
    path("meetup/<slug:meetup_slug>", views.meetup_detail, name= "meetup-detail")
]
