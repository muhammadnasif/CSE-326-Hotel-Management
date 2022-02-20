"""Hotel_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
import reception.views as reception_views
import reception.logInOut as reception_loginout
import reception.check_in as reception_checkin
import reception.customer as customerSearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reception_views.home, name='home'),
    path('getSingle/',reception_views.getSingle,name='getSingle'),
    path('login/', reception_loginout.LogIn, name='LogIn'),
    path('LogOut/', reception_loginout.LogOut, name='LogOut'),
    path('CheckIn/', reception_checkin.CheckIn, name='CheckIn'),
    path('addOtherBoarder/', reception_checkin.addOtherBoarder, name='addOtherBoarder'),
    path('undoOtherBoarder/', reception_checkin.undoOtherBoarder, name='undoOtherBoarder'),
    path('checkout/', reception_checkin.checkout, name='checkout'),
    path('customerSearch/', customerSearchView.customerSearch, name='customerSearch'),
    path('payDue/', reception_checkin.payDue, name='payDue'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
