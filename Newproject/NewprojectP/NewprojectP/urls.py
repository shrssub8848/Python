"""NewprojectP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home import views as v1
from about import views as v2
from login import views as v3
from signup import views as v4
from gallary import views as v5


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', v1.home, name='Home'),
    path('about/', v2.about, name='About'),
    path('login/', v3.login, name='Login'),
    path('signup/', v4.signup, name='Signup'),
    path('gallary/', v5.gallary, name='Gallary'),
    path('json/', v1.random, name='jhome'),
]
