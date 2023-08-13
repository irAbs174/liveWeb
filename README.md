liveWEB Project {form iran Open source society}{
    Development Team :: 174TEAM    MAHYAR
}
// start : 3 Feb 15:53
Lan : Python
fw : Django
face : html css
AND: js;
{%for keys in key%}{{keys.title}}{%endfor%}
class PageAdministrator(admin.ModelAdmin):
    fields = ['slug','title','content','author']


admin.site.register(PageAdmin, PageAdministrator)

