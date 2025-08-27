from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
# Create your views here.


def landing_main(request):
    return render(request, "views/main.html")

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings
    }
    return render(request, "views/home.html", context)

@login_required
def  list_view(request):
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        pass
    return render(request, 'views/list.html', {})