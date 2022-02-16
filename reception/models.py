import datetime

from django.db import models
# Create your models here.
from phonenumber_field.formfields import PhoneNumberField

class ROOM(models.Model):
    room_no = models.IntegerField()
    fare = models.IntegerField()
    capacity = models.IntegerField()
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return str(self.room_no)

class CUSTOMER(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    nid = models.CharField(max_length=20)
    email = models.EmailField()
    member_level = models.IntegerField()

    def __str__(self):
        return str(self.name)

class CUSTOMER_VISIT(models.Model):
    room_no = models.ForeignKey(ROOM, on_delete=models.CASCADE)             # Foreign KEY -> One to Many
    customer = models.ForeignKey(CUSTOMER, on_delete=models.CASCADE)
    total_bill = models.IntegerField()
    due_bill = models.IntegerField()
    check_in = models.DateTimeField(auto_now_add=True, blank=True)
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.check_in) + " | " + str(self.check_out) + " | " + str(self.customer)

class OTHER_BOARDER(models.Model):
    customer_visit = models.ForeignKey(CUSTOMER_VISIT, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)

    def __str__(self):
        return self.customer_name

class USER(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=20)   # designation

    def __str__(self):
        return self.username

class INVOICE(models.Model):
    customer_visit = models.OneToOneField(CUSTOMER_VISIT, on_delete=models.CASCADE)
    total_bill = models.IntegerField()

    def __str__(self):
        return str(self.customer_visit)
