from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    course = 'machine learning'
    Tclass = 21
    seat = 20
    cduration = '2.5 months'
    offering = {
        'c' : course, 
        'tl' : Tclass, 
        'st' : seat, 
        'cd' : cduration
        }
    return render(request, 'machine_learning/machine_learning.html', context=offering)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request, 'machine_learning/knn.html')

def dtree(request):
    return render(request, 'machine_learning/DT.html')