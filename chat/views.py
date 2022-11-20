from django.shortcuts import render


def index1(request):
    return render(request, 'index1.html', {})


def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })
