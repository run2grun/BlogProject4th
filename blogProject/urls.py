"""blogProject URL Configuration

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
from django.urls import path, include
import blogapp.views
import portfolioapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home' ),
    path('blog/', include('blogapp.urls')),
    path('blog/portfolio/', portfolioapp.views.portfolio, name='portfolio'),
    path('blog/portfolio/upload', portfolioapp.views.upload, name="upload"),
    path('blog/portfolio/create2', portfolioapp.views.create2, name="create2"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# FIXME: BASE.html 만들었는데 템플릿이 존재하지 않는다고 뜬다.
