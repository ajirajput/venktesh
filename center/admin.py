from django.contrib import admin
from .models import User, Doctor, Investigation, Investigation_Category, Category, RegistrationDetails, Registration
from django.utils.html import format_html

def active_selected_record(self, request, queryset):
    queryset.update(is_active=False)
def inactive_selected_record(self, request, queryset):
    queryset.update(is_active=True)
 


class RegistrationDetailsInline(admin.StackedInline):
    model = RegistrationDetails
    extra = 1
                  
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','consuitant_no','uhid_no','lab_no','reference_if_age','is_active','created_by','created_on']
    search_fields = ['name']
    inlines = [RegistrationDetailsInline]

    def save_model(self, request, obj, form, change):
        try:
            obj.Created_by = request.user
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)


class RegistrationDetailsAdmin(admin.ModelAdmin):
    list_display = ['name','registration','amount','get_registration_print']

    def get_registration_print(self, obj):
        if obj.name:
            return format_html(f'<a href="/center/print/{obj.pk}/" target="_blank">Print</a>')
        else:
            return format.format_html('-') 

    def save_model(self, request, obj, form, change):
        try:
            obj.Created_by = request.user
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class Investigation_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','status','is_active','created_by','created_on']
    search_fields = ['name']
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)


class InvestigationAdmin(admin.ModelAdmin):
    list_display = ['name','status','is_active','created_by','created_on']
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)

# class patientAdmin(admin.ModelAdmin):
#     list_display = []

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','mobile_no','status','is_active','created_by','created_on']
    search_fields = ['name']
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','role','status','is_active','created_by','created_on']
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as ex:
            print(ex)




admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RegistrationDetails,RegistrationDetailsAdmin)
admin.site.register(Investigation_Category,Investigation_CategoryAdmin)
admin.site.register(Investigation,InvestigationAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(User,UserAdmin)
admin.site.add_action(active_selected_record)
admin.site.add_action(inactive_selected_record)
  


