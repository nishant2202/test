from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("This is awesome")

# Create your views here.
