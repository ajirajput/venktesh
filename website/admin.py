from django.contrib import admin
from .models import Category, Service, ServiceDetails, GalleryDetails, Gallery, contact

# Register your models here.


class ServiceDetailsInline(admin.StackedInline):
    model = ServiceDetails
    extra = 1
    max_num = 1


class GalleryDetailsInline(admin.StackedInline):
    model = GalleryDetails
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_on']
    list_filter = ['created_by', 'created_on']
    list_per_page = 100
    search_fields = ['name']

    actions = ["active_selected_record", 'inactive_selected_record']

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        super().save_model(request, obj, form, change)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_by', 'created_on']
    list_filter = ['created_by', 'created_on']
    list_per_page = 100
    search_fields = ['name']
    inlines = [ServiceDetailsInline]

    actions = ["active_selected_record", 'inactive_selected_record']

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        super().save_model(request, obj, form, change)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_on']
    list_filter = ['created_by', 'created_on']
    list_per_page = 100
    search_fields = ['name']
    inlines = [GalleryDetailsInline]

    actions = ["active_selected_record", 'inactive_selected_record']

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        super().save_model(request, obj, form, change)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile_no', 'subject', 'message']
    list_per_page = 100
    search_fields = ['name']

    actions = ["active_selected_record", 'inactive_selected_record']

    def active_selected_record(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_selected_record(self, request, queryset):
        queryset.update(is_active=False)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(contact, ContactAdmin)

