from django.contrib import admin
from existingcustomer.models import ExistingCustomer
from existingcustomer.admin import ExistingCustomerAdmin
from newcustomer.models import NewCustomer

@admin.register(NewCustomer)
class NewCustomerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ExistingCustomerAdmin, self).get_queryset(request)
        if request.user.is_authenticated:
            return qs
        return qs(user=request.user.id)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False
    
    list_display = ['date','account_id','cx_name','email','phone','alternate_phone','pincode','state','plan_offered','price','disposition','remarks']
    exclude=('created_by',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by_id = request.user.id
        obj.save()






    
