
from django.contrib import admin

from authentication.models import CustomUser

from django.contrib.auth.models import Group

admin.site.unregister(Group)




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    admin.site.site_header='GST Service Center'

    def has_add_permission(self, request, obj=None):
        return False

    list_display= ['id','username','email','number','last_login','last_logout',]

    search_fields = ['username',] 










