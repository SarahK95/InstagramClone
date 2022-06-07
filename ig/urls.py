# from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.first,name='fistpage'),
    path('home/',views.home,name='ighome'),
    path('update-profile/',views.updateProfile,name='editProf'),
    path('upload/',views.uploadPicture,name='igFeed'),
    path('profile/',views.profilePage,name='instaProfile'),
    path('search/', views.search_results,name='search_results'),
    path('like/<int:image_id>',views.likes,name='likes'),
    path('comment/<int:image_id>',views.comments,name='comments'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)