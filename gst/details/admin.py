from django.contrib import admin
from details.models import  TanyaCustomerDetail, VikasCustomerDetail, AmanCustomerDetail

# Register your models here.

@admin.register(VikasCustomerDetail)
class VikasCustomerDetailAdmin(admin.ModelAdmin):
    list_display = ['id','date','cx_name','phone','email','pincode','state','disposition1','disposition2']

@admin.register(TanyaCustomerDetail)
class TanyaCustomerDetailAdmin(admin.ModelAdmin):
    list_display = ['id','date','cx_name','phone','email','pincode','state','disposition1','disposition2']

@admin.register(AmanCustomerDetail)
class AmanCustomerDetailAdmin(admin.ModelAdmin):
    list_display = ['id','date','cx_name','phone','email','pincode','state','disposition1','disposition2']


