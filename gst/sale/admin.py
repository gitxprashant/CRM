from django.contrib import admin

from sale.models import Sale

# Register your models here.

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ['account_id','cx_name','email','phone','alternate_phone','pincode','state','plan_offered','price','remarks']

    list_filter = ['created_by',]

    def get_queryset(self, request):
        qs = super(SaleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(disposition="10")
