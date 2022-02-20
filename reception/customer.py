from django.shortcuts import render


def customerSearch(request):
    return render(request,'reception/customerSearch.html')

