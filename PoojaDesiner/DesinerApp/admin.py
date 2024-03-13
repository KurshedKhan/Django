from django.contrib import admin

from DesinerApp.models import serviceBox 

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_heading','service_content')

# Register your models here.
admin.site.register(serviceBox,ServiceAdmin)
 