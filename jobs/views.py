from django.shortcuts import render

# get access to models
from .models import Job

def home(request):
    jobs = Job.objects       # it will get all the jobobjects from db and turn them to
                            # python objects and then u can use inside of the code
    return render(request, 'jobs/home.html', { 'jobs': jobs})
