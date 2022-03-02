"""Belle Musique Studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('favicon-32x32.png',
         RedirectView.as_view(url=staticfiles_storage.url('img/favicon-32x32.png'))),
    path('favicon-16x16.png',
         RedirectView.as_view(url=staticfiles_storage.url('img/favicon-16x16.png'))),
    path('site.webmanifest',
         RedirectView.as_view(url=staticfiles_storage.url('img/site.webmanifest'))),
    path('apple-touch-icon.png',
         RedirectView.as_view(url=staticfiles_storage.url('img/apple-touch-icon.png'))),
    path('safari-pinned-tab.svg',
         RedirectView.as_view(url=staticfiles_storage.url('img/safari-pinned-tab.svg'))),
    path('accounts/', include('allauth.urls')),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path('', include('home.urls')),
    path('products/', include('store.urls')),
    path('bag/', include('shopping_bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('lessons/', include('lessons.urls')),
    path('profiles/', include('profiles.urls')),
    path('workshops/', include('workshops.urls')),
    path('lessons/', include('lessons.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
