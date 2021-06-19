
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages



# Create your views here.




########### index ###########
def index(request):
    obj= add_work.objects.all()
    return render(request,'atly/index.html',{"img_details":obj})

def add_works(request):
    if request.method == "POST":
        form = add_work_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = add_work_form()
            messages.error(request, "ERROR FOUND!! Try Again")
    return render(request,'atly/add-work.html')


def blog(request,blog_id):
    obj = add_blog_table.objects.get(id=blog_id)

    if request.method == "POST":
        form = add_blog_form(request.POST, instance=obj)

        if form.is_valid():
            form.save()
        else:
            form = add_blog_form()
    return render(request,'atly/blog.html',{"img_details":obj})

def index_blog(request,blog_id):
    obj = add_work.objects.get(id=blog_id)

    if request.method == "POST":
        form = add_work_form(request.POST, instance=obj)

        if form.is_valid():
            form.save()
        else:
            form = add_work_form()
    return render(request,'atly/blog.html',{"img_details":obj})

def blog_full(request):
    obj= add_blog_table.objects.all()
    if request.method == "POST":
        req_id=request.POST.get("id")
        obj_delete=add_blog_table.objects.get(id=req_id)
        obj_delete.delete()
    return render(request,'atly/blog-full.html',{"img_details":obj})

def add_blog(request):
    if request.method == "POST":
        form = add_blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = add_blog_form()
            messages.error(request, "ERROR FOUND!! Try Again")
    return render(request,'atly/add-blog.html')


