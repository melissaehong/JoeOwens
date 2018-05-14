# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'anApp/index.html')

def about(request):
    return render(request, 'anApp/about.html')

def photo(request):
    return render(request, 'anApp/photo.html')

def contact(request):
    return render(request, 'anApp/contact.html')
