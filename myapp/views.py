from django.shortcuts import render

def home(request):
    return render(request, "myapp/home.html")

def primary_research(request):
    return render(request, "myapp/primary_research.html")

def secondary_research(request):
    return render(request, "myapp/secondary_research.html")
def causes(request):
    return render(request, "myapp/causes.html")
