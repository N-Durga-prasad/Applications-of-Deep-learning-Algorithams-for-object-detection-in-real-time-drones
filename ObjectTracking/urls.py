"""
URL configuration for ObjectTracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  User import views
from Admins import views as adv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #UserViews
    path("a/", views.base, name='base'),
    path('' , views.index , name='index'),
    path('userlogin/', views.userlogin , name='UserLogin'),
    path('Register/', views.Registration , name="Register"),
    path('UserHome/' , views.UserHome , name='UserHome'),
    path('stream/' , views.stream , name='stream'),
    path('video/' ,views.UploadVideo , name='video'),
    #Admin views
    path("AdminLogin/" , adv.AdminLogin , name='AdminLogin'),
    path('adminhome/' , adv.adminhome , name='adminhome'),
    path('viewusers/', adv.viewusers , name='viewusers'),
    path('Activateuser/' , adv.Activateuser , name='Activateuser'),
    path('DeleteUser/' , adv.DeleteUser , name='DeleteUser'),
] +static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)