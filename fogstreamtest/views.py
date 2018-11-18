from django.http import HttpResponse
from django.shortcuts import render
import pdb

def index(request):

    return render(request, 'index.html');