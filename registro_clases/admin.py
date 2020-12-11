from django.contrib import admin

from .models import Asignatura, TipoClase, Clase
# Register your models here.

class ClaseAdmin(admin.ModelAdmin):

    readonly_fields = [
        'maestro',
        'asignatura',
        'hora',
        'fecha',
    ]

    list_display = [
        'maestro',
        'asignatura',
        'fecha',
        'hora',
        'aprobada',
        'rechazada',
    ]

    list_filter = ['aprobada','rechazada']
    date_hierarchy = ('fecha')

admin.site.register(Clase,ClaseAdmin)

admin.site.register(Asignatura)

admin.site.register(TipoClase)