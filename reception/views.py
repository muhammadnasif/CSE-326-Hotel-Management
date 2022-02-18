from django.shortcuts import render
from reception.models import ROOM
from django.http import JsonResponse

# Create your views here.


def getSingle(request):
    print(request.GET)
    dict = []
    s = request.GET['s']
    d = request.GET['d']
    t = request.GET['t']
    a = request.GET['a']
    n = request.GET['n']
    dRoom = {}
    room = ROOM.objects.all()
    if s=="1":
        print('inside s==1')
        for r in room:
            if r.capacity == 1:
                dRoom['room_no'] = r.room_no
                dRoom['floor'] = r.floor
                dRoom['fare'] = r.fare
                dRoom['capacity'] = r.capacity
                dRoom['type'] = r.type
                dRoom['description'] = r.description
                dRoom['availability'] = r.availability
                if r.availability == 0:
                    dRoom['color'] = "green"
                elif r.availability == 1:
                    dRoom['color'] = "red"
                else:
                    dRoom['color'] = "yellow"
                dRC = dRoom.copy()
                dict.append(dRC)
    print(dict)
    return JsonResponse(dict,safe=False)

def home(request):
    dRoom1 = {}
    dRoom2 = {}
    dRoom3 = {}
    dRoom4 = {}
    dRoom5 = {}
    dRooms1 = []
    dRooms2 = []
    dRooms3 = []
    dRooms4 = []
    dRooms5 = []
    context = {}
    for r in ROOM.objects.all():
        if r.floor == 1:
            dRoom1['room_no'] = r.room_no
            dRoom1['floor'] = r.floor
            dRoom1['fare'] = r.fare
            dRoom1['capacity'] = r.capacity
            dRoom1['type'] = r.type
            dRoom1['description'] = r.description
            dRoom1['availability'] = r.availability
            if r.availability == 0:
                dRoom1['color'] = "green"
            elif r.availability == 1:
                dRoom1['color'] = "red"
            else:
                dRoom1['color'] = "yellow"
            dRC = dRoom1.copy()
            dRooms1.append(dRC)
        if r.floor == 2:
            dRoom2['room_no'] = r.room_no
            dRoom2['floor'] = r.floor
            dRoom2['fare'] = r.fare
            dRoom2['capacity'] = r.capacity
            dRoom2['type'] = r.type
            dRoom2['description'] = r.description
            dRoom2['availability'] = r.availability
            if r.availability == 0:
                dRoom2['color'] = "green"
            elif r.availability == 1:
                dRoom2['color'] = "red"
            else:
                dRoom2['color'] = "yellow"
            dRC = dRoom2.copy()
            dRooms2.append(dRC)
        if r.floor == 3:
            dRoom3['room_no'] = r.room_no
            dRoom3['floor'] = r.floor
            dRoom3['fare'] = r.fare
            dRoom3['capacity'] = r.capacity
            dRoom3['type'] = r.type
            dRoom3['description'] = r.description
            dRoom3['availability'] = r.availability
            if r.availability == 0:
                dRoom3['color'] = "green"
            elif r.availability == 1:
                dRoom3['color'] = "red"
            else:
                dRoom3['color'] = "yellow"
            dRC = dRoom3.copy()
            dRooms3.append(dRC)
        if r.floor == 4:
            dRoom4['room_no'] = r.room_no
            dRoom4['floor'] = r.floor
            dRoom4['fare'] = r.fare
            dRoom4['capacity'] = r.capacity
            dRoom4['type'] = r.type
            dRoom4['description'] = r.description
            dRoom4['availability'] = r.availability
            if r.availability == 0:
                dRoom4['color'] = "green"
            elif r.availability == 1:
                dRoom4['color'] = "red"
            else:
                dRoom4['color'] = "yellow"
            dRC = dRoom4.copy()
            dRooms4.append(dRC)
        if r.floor == 5:
            dRoom5['room_no'] = r.room_no
            dRoom5['floor'] = r.floor
            dRoom5['fare'] = r.fare
            dRoom5['capacity'] = r.capacity
            dRoom5['type'] = r.type
            dRoom5['description'] = r.description
            dRoom5['availability'] = r.availability
            if r.availability == 0:
                dRoom5['color'] = "green"
            elif r.availability == 1:
                dRoom5['color'] = "red"
            else:
                dRoom5['color'] = "yellow"
            dRC = dRoom5.copy()
            dRooms5.append(dRC)
    context['rooms1'] = dRooms1
    context['rooms2'] = dRooms2
    context['rooms3'] = dRooms3
    context['rooms4'] = dRooms4
    context['rooms5'] = dRooms5
    return render(request, 'reception/room.html', context)
