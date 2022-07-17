from django.contrib import admin
from .models import Customer, Status,Ticket, Fault, Transaction

# Register your models here.
admin.site.register(Status)
admin.site.register(Fault)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Transaction)
