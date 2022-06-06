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
    return render(request, 'registration/login.html', locals())

# homepage 
# @login_required(login_url='/accounts/login')
# def home(request):
#     likesForm = LikesForm
#     commentForm = CommentsForm
#     images = Image.objects.all()
#     user = request.user.get_username()
#     profile = Profile.objects.all()
#     likes = Likes.objects.all()
    
#     return render (request, 'home.html', locals())



    
