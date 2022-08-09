from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return  HttpResponse('This is the home page ()')


def about(request):
    return  HttpResponse('This is the about page (about/)')


def projects(request):
    return  HttpResponse('This is the projects page (projects/)')


def skills(request):
    return  HttpResponse('This is the skills page (skills/)')


def contact(request):
    return  HttpResponse('This is the contact page (contact/)')
