"""e_COMMERCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.urls import path
from django.views.generic import TemplateView

from APP import views
from APP.views import *
from e_COMMERCE import settings
from e_COMMERCE.settings import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index ),
    path('home/',Home),
    path('userregistration/',UserRegistration),
    path('userlogin/',UserLogin),
    path('register/',Register),
    path('logindetails/',LoginDetails),
    path('search/',SearchDetails),
    path('productdetails/',ProductDetails),
    path('forget/',Forget),
    path('forgetdetails/',ForgetDetails),
    path('newpassword/',NewPassword),
    path('addtocart/',AddTocart),
    path('logout/',LogOut),
    path('opencart/',OpenCart),
    path('remove/',Remove),
    path('contact_us/',ContactUs),
    path('contactdetails/',ContactDetails),




 ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
