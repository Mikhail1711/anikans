from django.contrib import admin

from journal.models import Journal, Supplies, Sales


class JournalAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class SuppliesAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class SalesAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Journal, JournalAdmin)
admin.site.register(Supplies, SuppliesAdmin)
admin.site.register(Sales, SalesAdmin)
