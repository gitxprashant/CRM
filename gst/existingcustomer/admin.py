
from calendar import c
from itertools import count
from django.contrib import admin
from psutil import users
from traitlets import default
from existingcustomer.models import ExistingCustomer
from newcustomer.models import NewCustomer

# Register your models here.
@admin.register(ExistingCustomer)
class ExistingCustomerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ExistingCustomerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user.id)
    
    list_display = ['account_id','cx_name','email','phone','alternate_phone','pincode','state','plan_offered','price','disposition','remarks']
    exclude = ('created_by',)


    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['created_by','date','disposition']
        else:
            return ['disposition','date']


    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True



    search_fields= ['email','phone','cx_name','account_id']
