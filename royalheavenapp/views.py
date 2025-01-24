from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def property(request):
    return render(request,'property.html')

def contact(request):
    return render(request,'contact.html')



def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = "New message from {}".format(name)

        # Compose the email
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send email
        send_mail(
            subject,
            full_message,
            email,  # From email
            [settings.EMAIL_HOST_USER],  # Your email address
        )
        return HttpResponse('Email sent successfully!')
    return render(request, 'base.html')  # Render the form if not POST