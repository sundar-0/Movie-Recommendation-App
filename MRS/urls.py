"""MRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from MovieRecommender import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('home/',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path("addmovie/",views.addmovie,name="addmovie"),
    path("logout/",views.user_logout,name="logout"),
    path("profile/",views.profile,name="profile")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
