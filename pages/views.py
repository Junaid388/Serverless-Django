import imp
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
HOME_PAGE_MSG = getattr(settings, "HOME_PAGE_MSG", "MISSING MESSAGE")

def home_view(request):
    return HttpResponse(f"<h1>{HOME_PAGE_MSG}</h1>")