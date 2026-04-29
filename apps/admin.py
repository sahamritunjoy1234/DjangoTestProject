from django.contrib import admin
from apps.models import Module
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.



class ModuleResource(resources.ModelResource):
    class Meta:
        use_bulk= True
        skip_diff = True
        batch_size= 1000
        model = Module
        import_id_fields = ("id",)
        
@admin.register(Module)
class ModuleAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = ModuleResource
    list_display = (
        "name",
        "updated_at",
        "created_at",
    )
    # inlines = [ModuleMappedRoleInline]  # Include the inline model