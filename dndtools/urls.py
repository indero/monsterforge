"""dndtools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from paperminis import views as paperminis_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paperminis.urls'))
]

#Add URL maps to redirect the base URL to our application

from django.views.generic import RedirectView

urlpatterns += [
    path('minis/', RedirectView.as_view(url='/')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', paperminis_view.signup, name='signup'),
    path('convert/', paperminis_view.convert_account, name='convert-account'),
    path('tempaccount/', paperminis_view.temp_account, name='temp-account'),
    path('profile/', paperminis_view.profile, name='profile'),
    path('accounts/delete/', paperminis_view.delete_account, name='delete-account'),

]