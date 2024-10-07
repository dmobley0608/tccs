from django.contrib import admin
from .models import WorkOrderRequest, WorkRequestResponse

# Register your models here.
class ResponseInline(admin.TabularInline):
    model = WorkRequestResponse
    
class WorkOrderRequestAdmin(admin.ModelAdmin):
    list_display=['created_at','customer_name', 'customer_email', 'customer_phone_number', 'status']
    readonly_fields=['created_at', 'updated_at', 'customer_request']
    sortable_by=['created_at', 'customer_name', 'customer_email','status']
    inlines=[ResponseInline]
    
admin.site.register(WorkOrderRequest, WorkOrderRequestAdmin)
