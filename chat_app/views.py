from django.shortcuts import render
from .models import Group,Chat
# Create your views here.


def index(request):
    return render(request, "chat_app/index.html")


def room(request, room_name):
    print("room name is " , room_name)
    room=Group.objects.filter(name=room_name).first()

    if room:
        pass
    else:
        room=Group(name=room_name)
        room.save()

    return render(request, "chat_app/room.html", {"room_name": room_name})
