from django.contrib import admin

from News.models import NewsBox


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    
admin.site.register(NewsBox,NewsAdmin)
# Register your models here.
