
from calendar import c
from django.contrib import admin

from authentication.models import CustomerDetail, Staff, CustomUser


admin.site.register(CustomUser)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display= ['user','email','phone']


@admin.register(CustomerDetail)
class CustomerDetailAdmin(admin.ModelAdmin):
    list_display = ['id','date','cx_name','phone','email','pincode','state','disposition1','disposition2']




