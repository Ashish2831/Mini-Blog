from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

def Home(request):
    posts = Post.objects.all()
    return render(request, "Blog/home.html", {'posts' : posts})

def About(request):
    return render(request, "Blog/about.html")

def Contact(request):
    return render(request, "Blog/contact.html")

def Dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, "The Page You Are Trying To Visit is Login Protected. ")
        return HttpResponseRedirect('/login/')
    posts = Post.objects.all()
    user = request.user
    full_name = user.get_full_name()
    gps = user.groups.all()
    return render(request, "Blog/dashboard.html", {'posts' : posts, 'full_name' : full_name, 'groups' : gps})

def Login(request):
    if not request.user.is_authenticated:
        emp_login = AuthenticationForm()
        if request.method == 'POST':
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                uname = login_form.cleaned_data.get('username')
                upass = login_form.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully!!")
                    return HttpResponseRedirect('/dashboard/')
            return render(request, "Blog/login.html", {'login' : login_form})
        return render(request, "Blog/login.html", {'login' : emp_login})
    else:
        return HttpResponseRedirect('/dashboard/')

def Logout(request):
    if not request.user.is_authenticated:
        messages.info(request, "The Page You Are Trying To Visit is Login Protected. ")
        return HttpResponseRedirect('/login/')
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return HttpResponseRedirect('/')

def Register(request):
    emp_register = Register_Form()
    if request.method == 'POST':
        register = Register_Form(request.POST)
        if register.is_valid():
            user = register.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            return render(request, "Blog/register.html", {'register': register, 'success' : 'Successfully Registered!!'})
        else:
            return render(request, "Blog/register.html", {'register': register})
    return render(request, "Blog/register.html", {'register': emp_register})

def AddPost(request):
    if not request.user.is_authenticated:
        messages.info(request, "The Page You Are Trying To Visit is Login Protected. ")
        return HttpResponseRedirect('/login/')

    emp_post_form = Post_Form()
    if request.method == "POST":
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post_form.save()
        else:
            return render(request, 'Blog/addpost.html', {'post_form' : post_form})
        return render(request, 'Blog/addpost.html', {'post_form' : post_form, 'success' : 'Post Added Successfully!!'})
    return render(request, 'Blog/addpost.html', {'post_form' : emp_post_form})

def UpdatePost(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "The Page You Are Trying To Visit is Login Protected. ")
        return HttpResponseRedirect('/login/')

    if request.method == "POST":
        post = Post.objects.get(pk=id)
        post_form = Post_Form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'Blog/updatepost.html', {'post_form' : post_form, 'success' : 'Post Updated Successfully!!'})
        else:
            post_form = Post_Form(request.POST)
            return render(request, 'Blog/updatepost.html', {'post_form' : post_form})
    else:
        post = Post.objects.get(pk=id)
        post_form = Post_Form(instance=post)
        return render(request, 'Blog/updatepost.html', {'post_form' : post_form})

def DeletePost(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "The Page You Are Trying To Visit is Login Protected. ")
    return HttpResponseRedirect('/login/')
    post = Post.objects.get(pk=id)
    post.delete()
    messages.success(request, "Post Deleted Successfully!!")
    return HttpResponseRedirect('/dashboard/')
