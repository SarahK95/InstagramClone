from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, views, forms
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import LikesForm, CommentsForm, UpdateProfileForm, UploadPicForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.

# first page user sees basically loginpage
def first(request):
    form = forms.AuthenticationForm
    return render(request, 'registration/login.html', {'form':form})

# homepage 
@login_required(login_url='/accounts/login')
def home(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    profile = Profile.objects.all()
    likes = Likes.objects.all()
    
    context ={
        'likesForm':likesForm,
        'commentForm':commentForm,
        'images':images,
        'user':user,
        'profile':profile,
        'likes':likes
    }
    
    return render (request, 'home.html', context)

def likes(request, image_id):
    likesForm = LikesForm()
    post = Likes.objects.create(user=request.user, image=get_object_or_404(Image, pk=image_id),likes=1)
    post.save()
    print(post)
    return redirect('ighome')

def comments(request, image_id):
    commentsForm = CommentsForm()
    if request.method =='POST':
        commentsForm = CommentsForm(request.POST)
        if commentsForm.is_valid():
            form = commentsForm.save(commit=False)
            form.user=request.user
            form.image = get_object_or_404(Image, pk=image_id)
            form.save()
    return redirect ('ighome') 

@login_required(login_url='/accounts/login')
def profilePage(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    current_user = request.user
    cphoto = Image.objects.filter(profile=current_user.id)
    profile = Profile.objects.all()
    likes = Likes.objects.all()
    
    context ={
        'likesForm':likesForm,
        'commentForm':commentForm,
        'images':images,
        'user':user,
        'profile':profile,
        'likes':likes,
        'cphoto':cphoto
    }
    
    return render (request, 'profile.html', context)
           
    



    
