from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Projects
# Create your views here.
def index(request):
    return render(request,"DevPortfolio/index.html")

def skill(request):
    return render(request,"DevPortfolio/skill.html")
def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('useremail')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')

        send_mail(
            f"New Contact Form Submission from {firstname} {lastname}",
            message,
            email,
            ['talhazunair37@gmail.com'],
            fail_silently=False
        )
        return HttpResponseRedirect('/')

    return render(request, "DevPortfolio/contact.html")
def about(request):
    return render(request,"DevPortfolio/about.html")

def project(request):
    about_project = Projects.objects.all()
    return render(request,"DevPortfolio/project.html",{
        'about_project':about_project
    })

def projectdetail(request,id):
    get_detail = get_object_or_404(Projects,id=id)
    return render(request,"DevPortfolio/projectdetail.html",{
        "project":get_detail
    })
