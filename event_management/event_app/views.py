from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request, 'gallery.html')
def booking(request):
    return render(request, 'booking.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request,'home.html')


def samphttp(request,name,year,branch):
    d={
        "Name":name,
        'Year':year,
        'Branch':branch,
    }
    return JsonResponse(d)
# create same for about,events,booking,contact