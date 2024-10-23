from django.shortcuts import render
from django.http import HttpResponse  # Create your views here.


def index(request):
    meetups = [
        {"title": "first meetup", "location": "Paris", "slug": "a-first-meetup"},
        {"title": "second meetup", "location": "New York", "slug": "a-second-meetup"},
    ]

    return render(request, "meeting/index.html", {
        "show_meetup": False,
        "meetup": meetups
    })


def meetup_detail(request):
    meetup_detail = {
        "title": "Dilluminati",
        "description": "meetup will be on this time and at this date BOOK NOW",
        }

    return render(request, "meeting/detail.html", {
        "title": meetup_detail["title"],
        "description": meetup_detail["description"]
    })
