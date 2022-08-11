from django.shortcuts import render, HttpResponse
from home.models  import Contact

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
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        contact = Contact(name=name,  email=email, subject=subject, message=message)
        contact.save()
        print("The data has been written to the DB.")
    return render(request, 'contact.html')
