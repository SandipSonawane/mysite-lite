from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from Top_Skills.dash_app import *


def index(request):
    return render(request, 'My_Portfolio/index.html')

