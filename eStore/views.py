from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Ticket,Fault,Customer,Status, Transaction
from users import urls
from django.views.decorators.cache import cache_control


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True)
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return render(request,'Logout.html')

def tickets(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            i = request.POST['searchticket']
            return render(request, 'tickets.html', {"Tickets": Ticket.objects.filter(id = i)})
        return render(request, 'tickets.html' ,{
                "Tickets": Ticket.objects.all().order_by('date').reverse()[:10]
            })
    else:
            return render(request, 'Logout.html')

def searchticket(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST['searchticket']
            return render(request, 'searchticket.html',{
                "data":data
            })
    else:
            return render(request, 'Logout.html')

def addcustomer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            i = Customer(name= request.POST['name'],phonenumber= request.POST['phonenumber'],email= request.POST['email'])
            i.save()
            return HttpResponseRedirect(reverse('maketicket'))
        else:
            return render(request, 'addcustomer.html',{
                "Tickets": Ticket.objects.all(),
                "Fault": Fault
        })
    else:
            return render(request, 'Logout.html')

def ticketdetails(request, ticketID):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ticketdata = Ticket.objects.get(pk = ticketID)
            return render(request, 'ticketdetails.html', {
                "ticketdata": ticketdata,
                "Status": Status.objects.all()
            })
    else:
            return render(request, 'Logout.html')

def maketicket(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            i = Ticket(customer = Customer.objects.get(pk = request.POST.get('customer',False)),
                        fault = Fault.objects.get(pk =  request.POST.get('fault_data',False)),
                        status = Status.objects.get(pk =  request.POST.get('status_data',False)),
                        description = request.POST.get('descriptiondata',False),
                        device = request.POST.get('device_data',False),
                        transaction = Transaction.objects.get(pk = request.POST.get('amount_data',False)),
                        amount = request.POST.get('amount',False))
            i.save()

            return render(request, 'maketicket.html',{
            "Tickets":Ticket.objects.all(),
            "Fault": Fault.objects.all(),
            "Customer": Customer.objects.all(),
            "Status": Status.objects.all(),
            "Transaction": Transaction.objects.all()
            })
        else:
            return render(request, 'maketicket.html',{
            "Tickets":Ticket.objects.all(),
            "Fault": Fault.objects.all(),
            "Customer": Customer.objects.all(),
            "Status": Status.objects.all(),
            "Transaction": Transaction.objects.all()
            })
    else:
            return render(request, 'Logout.html')

def searchcustomer(request):
    if request.user.is_authenticated:
        return render(request, 'searchcustomer.html',{
            "Customer": Customer.objects.all()
        })
    else:
        return render(request, 'Logout.html')

def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')

def addfault(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST['fault'])
            i = Fault(name = request.POST['fault'])
            i.save()
            return HttpResponseRedirect(reverse('maketicket'))
        return render(request, 'addfault.html')
    else:
            return render(request, 'Logout.html')

def addstatus(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST['status'])
            i = Status(name = request.POST['status'])
            i.save()
            return HttpResponseRedirect(reverse('maketicket'))
        return render(request, 'addstatus.html')
    else:
            return render(request, 'Logout.html')

def adddata(request):
    if request.user.is_authenticated:
        Data =Ticket.objects.all()
        result = 0
        for data in Data:
            result = data.amount + result
            print(data.amount)
        print("Total is ", result)
        return render(request, 'about.html')
    else:
            return render(request, 'Logout.html')

def loginview(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['loginemail']
            password = request.POST['loginpassword']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Login Success")
                login(request, user)
                return HttpResponseRedirect(reverse('tickets'))
            else:
                print("Login Failed")

        return HttpResponseRedirect(reverse('homepage'))

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponsePermanentRedirect(reverse("navigate"))
    else:
            return render(request, 'Logout.html')

def changestatus(request):
    if request.method == "POST":
        changestatus = request.POST.get('status_data', False)
        changeticket = request.POST.get('ticket_data', False)
        Ticket.objects.select_for_update().filter(pk = changeticket).update(status= Status.objects.get(pk = changestatus))
        return HttpResponseRedirect(reverse('tickets'))



