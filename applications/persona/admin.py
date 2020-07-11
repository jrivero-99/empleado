from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departameto',
        'job',
        'full_name',
    )
    #
    def full_name(self, obj):
        # toda la operación que necesite
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ('departameto','job','habilidades')
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)