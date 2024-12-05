from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'valoracion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_filter = ('valoracion', 'fecha_modificacion')


# Register your models here.
