from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def property(request):
    return render(request,'property.html')

def contact(request):
    return render(request,'contact.html')
