'''Root URL Configuration
'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('unique/', admin.site.urls),
    path('',include('Home.urls')),
    path('accounts/',include('django.contrib.auth.urls'))
]
