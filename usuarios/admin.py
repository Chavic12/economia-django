from django.contrib import admin
from economia.models import IndicadorEconomico
# Register your models here.
class IndicadorEconomicoAdmin(admin.ModelAdmin):
    list_display = ('municipio', 'anio', 'presupuesto_anual', 'monto_residencial', 'monto_residencial_industrial', 'presupuesto_campañas', 'ingresos_fiscales', 'ingresos_preasignaciones', 'ingresos_credito', 'ingresos_asistencia', 'ingresos_anticipos', 'ingresos_totales', 'ingresos_ambiental_fiscales', 'ingresos_ambiental_preasignaciones', 'ingresos_totales_ambiental')

admin.site.register(IndicadorEconomico, IndicadorEconomicoAdmin)