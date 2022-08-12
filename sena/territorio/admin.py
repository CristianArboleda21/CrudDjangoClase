from re import A
from django.contrib import admin
from .models import Aprendiz
from .models import Monitoria
from .models import Actividades

# Register your models here.
@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ('id','cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'edad')
    search_fields = ["cedula"]

    def edad(self, obj):
        from datetime import date
        hoy = date.today()

        edad = hoy.year - obj.fecha_nacimiento.year - ((hoy.month, hoy.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))
        return edad


@admin.register(Monitoria)
class MonitoriaAdmin(admin.ModelAdmin):
    list_display = ('id','cat', 'cedula', 'aprendiz','apellido', 'fecha_Inicio', 'fecha_Final', )
    search_fields = ["cat", "aprendiz__nombre"]
    list_filter = ['cat', 'fecha_Inicio']
    list_editable = ['aprendiz']

    def cedula(self,obj):
        return obj.aprendiz.cedula

    def nombre(self,obj):
        return obj.aprendiz.nombre

    def apellido(self,obj):
        return obj.aprendiz.apellido

@admin.register(Actividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('monitor', 'actividad_Realizada', 'obs', 'fecha', )
    search_fields = ['actividadRealizada']


"""
admin.site.register(Aprendiz, AprendizAdmin)
admin.site.register(Monitoria)
admin.site.register(Actividades)
"""

