from django.contrib import admin

from .models import Maestro

# Register your models here.

class MaestroAdmin(admin.ModelAdmin):

    search_fields = [
        'nombres',
        'apellidos',
    ]
    list_display = [
        '__str__',
        'email',
        'es_admin',
    ]

admin.site.register(Maestro,MaestroAdmin)