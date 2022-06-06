from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, views, forms
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import LikesForm, CommentsForm, UpdateProfileForm, UploadPictureForm
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

@login_required(login_url='/accounts/login')
def updateProfile(request):
    current_user = request.user
    myprof = Profile.objects.get(user=current_user.id)
    updateForm = UpdateProfileForm(instance=request.user)
    if request.method == 'POST':
        updateForm = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if updateForm.is_valid():
            updateForm.save()     
        return redirect('instaProfile')
    else:
        updateForm = UpdateProfileForm(instance=request.user.profile)
    return render(request,'update_profile.html', {'myprof':myprof})

@login_required(login_url='/accounts/login')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:  
        images = Image.objects.all()
        user = request.user.get_username()
        profile = Profile.objects.all()
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"
        photos = Image.objects.filter(profile=User.objects.get(username=search_term))
        print(User.objects.get(username=search_term))
        return render(request, 'search.html',{'images':images, 'user':user, 'profile':profile, 'searches_users':searched_users, 'message':message, 'photos':photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})
    
    
@login_required(login_url='/accounts/login')
def uploadPicture(request):
    current_user = request.user
    uploadForm = UploadPictureForm()
    print(uploadForm)
    if request.method == 'POST':
        uploadForm = UploadPictureForm(request.POST,request.FILES)
        user = request.user.id
        if uploadForm.is_valid():
            upload = uploadForm.save(commit=False)
            upload.user = request.user.profile
            upload.profile = current_user
            upload.save()    
        return redirect('instaProfile', {'user': user})
    else:
            uploadForm = UploadPictureForm()
    return render(request,'upload_picture.html', locals())    
    
           
    



    
