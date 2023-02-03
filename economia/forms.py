from django import forms
from .models import Municipio
from django import forms
from .models import IndicadorEconomico, IndicadorAmbiental, IndicadorInstitucional, IndicadorSocial

class MunicipalitySelectionForm(forms.Form):
    municipio = forms.ModelChoiceField(
        queryset=Municipio.objects.all(),
        empty_label="Seleccione un municipio",
        to_field_name="nombre",
        widget=forms.Select(attrs={'class': 'form-control'})
    )



class IndicadorEconomicoForm(forms.ModelForm):
    class Meta:
        model = IndicadorEconomico
        fields = ['municipio', 'anio', 'presupuesto_anual', 'monto_residencial', 'monto_residencial_industrial', 'presupuesto_campañas', 'ingresos_fiscales', 'ingresos_preasignaciones', 'ingresos_credito', 'ingresos_asistencia', 'ingresos_anticipos', 'ingresos_totales', 'ingresos_ambiental_fiscales', 'ingresos_ambiental_preasignaciones', 'ingresos_totales_ambiental']

class IndicadorAmbientalForm(forms.ModelForm):
    class Meta:
        model = IndicadorAmbiental
        fields = ['municipio', 'anio', 'area_sanitarios', 'num_botaderos', 'area_botaderos', 'total_residuos_tone', 'total_residuos_solidos', 'total_residuos_peligroso_ton', 'total_residuos_organicos_ton', 'total_residuos_inorganicos_ton', 'total_residuos', 'residuos_urbanos_reciclaje', 'total_residuos_urbanos', 'total_residuos_solidos_peligrososo', 'captacion_agua_superficial', 'captacion_agua_subterranea', 'volumen_total_superficial_subterranea', 'volumen_bruto_dulce', 'volumen_agua_usuario', 'total_agua_residual_recolectada', 'total_residual_tratamiento', 'num_plantas_tratamiento_residual', 'capacidad_tratamiento_residual', 'total_agua_notratada_m3', 'total_agua_tratada_vertida', 'total_agua_no_tratada_vertida', 'catidad_agua_residual_alcatarillado_m3', 'consumo_agua']


class IndicadorInstitucionalForm(forms.ModelForm):
    class Meta:
        model = IndicadorInstitucional
        fields = ['municipio', 'anio', 'funcionarios_tiempo_completo', 'cobertura_km_barrido_publicas', 'personas_servicio_barrido', 'personas_gestion_ambiental', 'energia_kWh', 'energia_valor', 'combustible_diesel', 'combustible_extra', 'combustible_super', 'num_productos', 'num_cortes_servicio']




class IndicadorSocialForm(forms.ModelForm):
    class Meta:
        model = IndicadorSocial
        fields = ['municipio', 'anio', 'num_vehiculos', 'capacidad_tone_vehiculos', 'porcentaje_barrido', 'km_barrido', 'porcentaje_barrido_urbanas', 'porcentaje_barrido_rurales', 'porcentaje_residuos', 'proyectos_conservacion_agua', 'abast_agua_horas', 'area_m2_institucion', 'area_m2_parques', 'area_m2_plazas', 'area_m2_jardines', 'area_m2_parterres', 'area_m2_riberas', 'area_m2_estadios', 'area_m2_canchas', 'area_m2_urbanas', 'area_total_hect']

