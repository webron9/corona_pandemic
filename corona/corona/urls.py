"""corona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.contrib.auth import views
from my_app.my_script import populate_stat,populate_news
from  my_app.views import signUp
populate_stat()
populate_news()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_app.urls')),
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('accounts/signup/',signUp,name='signup'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': settings.LOGOUT_REDIRECT_URL}),
]

## sanket -> i@mWebron9 superuser
## sanket -> i@mWebron9
## test4 -> i@mSanket9
## test1 -> password superuser