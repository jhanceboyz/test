from django.db import models
from django.db.models.base import Model

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField( max_length=254)
    phonenumber = models.CharField(max_length=12)
    

    def __str__(self):
        return f"{self.name} {self.phonenumber}"


class Fault(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Transaction(models.Model):
    type = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.type}"

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name="numberoftickets")
    fault = models.ForeignKey(Fault, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True, null=True)
    device = models.CharField(max_length=50)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name}______{self.device}______{self.status}______{self.date}"

