from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.first,name='firstpage'),
    path('home/',views.home,name='ighome'),
    path('search/', views.search_results,name='search_results'),
    path('edit/',views.updateProfile,name='editProf'),
    path('profile/',views.profilePage,name='instaProfile'),
    path('like/<int:image_id>',views.likes,name='likes'),
    path('comment/<int:image_id>',views.comments,name='comments'),
    path('upload/',views.uploadPicture,name='igFeed'),
       
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)