import datetime

from django.db.models import Count, Q
from django.http import JsonResponse
from .models import *
from django.core import serializers


# Check in form creates s new customer and a customer visit. First checks if the
# customer exists or not. If the customer exists then the customer will be not
# created and only the customer visit will be instantiated.
# Status codes
# 0 -> Customer Visit Exists
#
def CheckIn(request):
    context = {}
    print(request.GET)
    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']
    address = request.GET['address']
    nid = request.GET['nid']
    room = request.GET['room']
    memberLevel = 1
    print(request.GET)
    # checks if the boarder exists or not. If the boarder exists then only creates a
    # CUSTOMER_VISIT instance of that corresponding boarder
    boarder_exists = CUSTOMER.objects.filter(phone=phone).exists()
    customer_visit_exist = CUSTOMER_VISIT.objects.filter(customer__phone=phone).exists()

    if name == '' or phone == '' or nid == '' or address == '':
        context['status'] = 3

    elif customer_visit_exist:
        print("this customer is already staying in the hotel")
        context['status'] = 0
    elif boarder_exists:
        print(f'The boarder exists {boarder_exists}')

        # this room is used as dummy as for now. room no would be fetched from the
        # frontend.
        # #################################
        room = ROOM.objects.get(room_no=room)
        room.availability = 1
        room.save()
        # #################################
        boarder = CUSTOMER.objects.get(phone=phone)
        customer_visit = CUSTOMER_VISIT(room_no=room, customer=boarder, total_bill=room.fare, due_bill=room.fare)
        customer_visit.save()
        context['status'] = 1

    else:
        boarder = CUSTOMER(name=name, phone=phone, address=address, nid=nid, email=email, member_level=memberLevel)
        boarder.save()
        # ##################################
        room = ROOM.objects.get(room_no=room)
        room.availability = 1
        room.save()
        # ##################################
        customer_visit = CUSTOMER_VISIT(room_no=room, customer=boarder, total_bill=room.fare, due_bill=room.fare)
        customer_visit.save()
        context['status'] = 2

    return JsonResponse(context)


# Saves the other boarders of the corresponding customer visit
# To find which customer is currently is in the hotel we search
# in the table for those RECORDS whose check_out fields are NONE
# status -- 1 => Other Boarder added successfully
def addOtherBoarder(request):
    context = {}
    print(request.GET)
    phone = request.GET['phone']
    name = request.GET['name']
    room = request.GET['room']
    # customer_visit = CUSTOMER_VISIT.objects.get(customer__phone=phone, check_out=None)
    # otherBoarder = OTHER_BOARDER.objects.filter(customer_visit_id = customer_visit.id)
    # print(otherBoarder)
    if name != '':
        customer_visit = CUSTOMER_VISIT.objects.get(room_no__room_no=room, check_out=None)
        otherBoarder = OTHER_BOARDER(customer_visit=customer_visit, customer_name=name)
        otherBoarder.save()

        tempOtherBoarder = request.session['undo_otherBoarder_list']
        tempOtherBoarder.append(otherBoarder.id)
        request.session['undo_otherBoarder_list'] = tempOtherBoarder

        allOtherBoarder = OTHER_BOARDER.objects.filter(customer_visit_id=customer_visit.id)
        allOtherBoarder = serializers.serialize('json', allOtherBoarder)

        context = {
            'name': customer_visit.customer.name,
            'id': request.GET['room'],
            'status': 1,
            'otherBoarder': allOtherBoarder,
        }
    else:
        context['status'] = 0

    return JsonResponse(context)


def undoOtherBoarder(request):
    tempList = request.session['undo_otherBoarder_list']
    print(tempList)
    print(request.GET)
    if len(tempList) == 0:
        return JsonResponse({})
    else:
        room = request.GET['room']
        undoID = tempList.pop()
        request.session['undo_otherBoarder_list'] = tempList

        otherBoarder = OTHER_BOARDER.objects.get(id=undoID)
        print(otherBoarder)
        otherBoarder.delete()

        phone = request.GET['phone']
#         customer_visit = CUSTOMER_VISIT.objects.get(customer__phone=phone, check_out=None)
        customer_visit = CUSTOMER_VISIT.objects.get(room_no__room_no=room, check_out=None)
        allOtherBoarder = OTHER_BOARDER.objects.filter(customer_visit_id=customer_visit.id)
        allOtherBoarder = serializers.serialize('json', allOtherBoarder)

        context = {
            'otherBoarder': allOtherBoarder,
            'status': 1,
            'id': request.GET['room'],
        }
        return JsonResponse(context)


def checkout(request):
    context = {}
    name = request.GET['room']
    phone = request.GET['phone']
    thisTime = datetime.datetime.now()
    CreateInvoice(name, phone, thisTime)

    return JsonResponse(context)

def CreateInvoice(name, phone, dateTime):
    customer_visit = CUSTOMER_VISIT.objects.get(check_out=None, customer__phone=phone)
    print(customer_visit)

    checkin = customer_visit.check_in
    checkout = dateTime
    customer_name = name
    total_bill = customer_visit.total_bill
    otherBoarder = []

    queryBoarder = OTHER_BOARDER.objects.filter(customer_visit_id=customer_visit.id)

    for boarder in queryBoarder:
        otherBoarder.append(boarder.customer_name)




