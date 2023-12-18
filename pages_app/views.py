from django.shortcuts import render 
from django.http import Http404
database = [
    {
        'name':'parsa',
        'last name':'nazer',
        'number':'09051349047'
    },
    {
        'name':'mansour',
        'last name':'marzban',
        'number':'01708045115'
    }
]
# Create your views here.

def base_page(request):
    return render(request, "pages_app/base.html")
def home_page(request, name):
    for person in database:
        if name == person['name']:
            return render(request, "pages_app/home.html", context={'name': person['name'],'number': person['number']}) #address 
    raise Http404("user does not exist")
def users(request):
    return render(request,'pages_app/users', context={'database': database})