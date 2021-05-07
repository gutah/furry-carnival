import requests
from django.shortcuts import render
from django.urls import reverse
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request,'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    requested_search = {
        'search':search
    }
    return render(request,'my_app/new_search.html', requested_search )
