from django.contrib import admin
from .models import PageAdmin

class PageAdministrator(admin.ModelAdmin):
    fields = ['slug','title','content','author']


admin.site.register(PageAdmin, PageAdministrator)

