from django.shortcuts import render
from .models import post

# Create your views here.
'''
    view : 
        - url
        - model
        - tempate
'''

def post_list(request):
    data = post.objects.all() # model
    return render(request,'posts_list.html', {'posts':data})
