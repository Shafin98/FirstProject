from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def chilling(request):
    return render(request, 'blogs/blogs.html')