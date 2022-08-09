from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    # return  HttpResponse('This is the home page ()')
    context = {'name': 'Qingying', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return  HttpResponse('This is the about page (about/)')
    return render(request, 'about.html')


def projects(request):
    # return  HttpResponse('This is the projects page (projects/)')
    return render(request, 'projects.html')


def skills(request):
    # return  HttpResponse('This is the skills page (skills/)')
    return render(request, 'skills.html')


def contact(request):
    # return  HttpResponse('This is the contact page (contact/)')
    return render(request, 'contact.html')
