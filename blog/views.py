from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs

# Create your views here.

def all_blogs(request):
    blog = Blogs.objects.all()
    # blog = Blogs.objects.order_by(-date)[:5]
    #".order_by(-date)" sort the objects by date. newest to oldest
    #"[:5]" limits the object by 5
    return render(request, 'blog/all_blogs.html', {'blog':blog})
