"""Django_Playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
## Use include() to add URLS from the different applications
from django.conf.urls import url, include
from django.contrib import admin

## Add URL maps to redirect the base URL to a specific application
from django.views.generic import RedirectView

## each url() function associates a URL pattern to a specific view or with another list of URL pattern testing code
## first route to admin/ module which has Admin URL mapping definitions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.Login_Reg.urls')),
    #url(r'^catalog/', include('catalog.urls')),
    ## Redirects base URL to login app
    #url(r'^$', RedirectView.as_view(url='/login/', permanent=True)),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
## ^ Use static() to add url mapping to server static files during development (only)
