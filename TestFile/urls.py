"""TestFile URL Configuration

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
from django.urls import path, include
from testfileapp import views

from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.red, name='redirect'),
    path('upfile/', views.home, name='home'),
    path('upfile/sign_up', views.sign_up, name='sign_up'),
    path('upfile/sign_in', LoginView.as_view(template_name='testfileapp/sign_in.html'), name='sign_in'),
    path('upfile/sign_out', LogoutView.as_view(next_page='/'), name='sign_out'),
    path('upfile/social_auth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
