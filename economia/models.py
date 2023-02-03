from django.db import models
from django.db.models import Max, Min,Avg
from imagekit.models import ImageSpecField

# Create your models here.


class Municipio(models.Model):
    idMunicipios = models.IntegerField(primary_key=True, default='some_value')
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    contrasenia = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.nombre

class IndicadorEconomico(models.Model):
    id_economico = models.AutoField(primary_key=True)
    municipio = models.ForeignKey('Municipio', on_delete=models.PROTECT, default="")
    anio = models.IntegerField(default=2020)
    presupuesto_anual = models.DecimalField(max_digits=12, decimal_places=2)
    monto_residencial = models.DecimalField(max_digits=12, decimal_places=2)
    monto_residencial_industrial = models.DecimalField(max_digits=12, decimal_places=2)
    presupuesto_campañas = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_fiscales = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_preasignaciones = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_credito = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_asistencia = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_anticipos = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_totales = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_ambiental_fiscales = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_ambiental_preasignaciones = models.DecimalField(max_digits=12, decimal_places=2)
    ingresos_totales_ambiental = models.DecimalField(max_digits=12, decimal_places=2)
    subindice = models.DecimalField(max_digits=12, decimal_places=2, default=0)
   
    def calculate_subindice(self):
        min_presupuesto = IndicadorEconomico.objects.all().aggregate(Min('presupuesto_anual'))['presupuesto_anual__min']
        max_presupuesto = IndicadorEconomico.objects.all().aggregate(Max('presupuesto_anual'))['presupuesto_anual__max']
        presupuesto_normalized = 9 * ((float(self.presupuesto_anual) - float(min_presupuesto)) / (float(max_presupuesto) - float(min_presupuesto))) + 1

        min_monto_residencial = IndicadorEconomico.objects.all().aggregate(Min('monto_residencial'))['monto_residencial__min']
        max_monto_residencial = IndicadorEconomico.objects.all().aggregate(Max('monto_residencial'))['monto_residencial__max']
        monto_residencial_normalized = 9 * ((float(self.monto_residencial) - float(min_monto_residencial)) / ( float(max_monto_residencial) - float(min_monto_residencial))) + 1

        min_monto_residencial_industrial = IndicadorEconomico.objects.all().aggregate(Min('monto_residencial_industrial'))['monto_residencial_industrial__min']
        max_monto_residencial_industrial = IndicadorEconomico.objects.all().aggregate(Max('monto_residencial_industrial'))['monto_residencial_industrial__max']
        monto_industrial_nomalized = 9 * ((float(self.monto_residencial_industrial) - float(min_monto_residencial_industrial)) / (float(max_monto_residencial_industrial) - float(min_monto_residencial_industrial))) + 1

        min_ingresos_fiscales = IndicadorEconomico.objects.all().aggregate(Min('ingresos_fiscales'))['ingresos_fiscales__min']
        max_ingresos_fiscales = IndicadorEconomico.objects.all().aggregate(Max('ingresos_fiscales'))['ingresos_fiscales__max']
        ingresos_fiscales_nomalized = 9 * ((float(self.ingresos_fiscales) - float(min_ingresos_fiscales)) / (float(max_ingresos_fiscales) - float(min_ingresos_fiscales))) + 1

        min_ingresos_preasignaciones = IndicadorEconomico.objects.all().aggregate(Min('ingresos_preasignaciones'))['ingresos_preasignaciones__min']
        max_ingresos_preasignaciones = IndicadorEconomico.objects.all().aggregate(Max('ingresos_preasignaciones'))['ingresos_preasignaciones__max']
        ingresos_preasignaciones_nomalized = 9 * ((float(self.ingresos_preasignaciones) - float(min_ingresos_preasignaciones)) / (float(max_ingresos_preasignaciones) - float(min_ingresos_preasignaciones))) + 1

        min_ingresos_credito = IndicadorEconomico.objects.all().aggregate(Min('ingresos_credito'))['ingresos_credito__min']
        max_ingresos_credito = IndicadorEconomico.objects.all().aggregate(Max('ingresos_credito'))['ingresos_credito__max']
        ingresos_credito_nomalized = 9 * ((float(self.ingresos_credito) - float(min_ingresos_credito)) / (float(max_ingresos_credito) - float(min_ingresos_credito))) + 1

        min_ingresos_asistencia = IndicadorEconomico.objects.all().aggregate(Min('ingresos_asistencia'))['ingresos_asistencia__min']
        max_ingresos_asistencia = IndicadorEconomico.objects.all().aggregate(Max('ingresos_asistencia'))['ingresos_asistencia__max']
        ingresos_asistencia_nomalized = 9 * ((float(self.ingresos_asistencia) - float(min_ingresos_asistencia)) / (float(max_ingresos_asistencia) - float(min_ingresos_asistencia))) + 1

        min_ingresos_anticipos = IndicadorEconomico.objects.all().aggregate(Min('ingresos_anticipos'))['ingresos_anticipos__min']
        max_ingresos_anticipos = IndicadorEconomico.objects.all().aggregate(Max('ingresos_anticipos'))['ingresos_anticipos__max']
        ingresos_anticipos_nomalized = 9 * ((float(self.ingresos_anticipos) - float(min_ingresos_anticipos)) / (float(max_ingresos_anticipos) - float(min_ingresos_anticipos))) + 1

        min_ingresos_totales = IndicadorEconomico.objects.all().aggregate(Min('ingresos_totales'))['ingresos_totales__min']
        max_ingresos_totales = IndicadorEconomico.objects.all().aggregate(Max('ingresos_totales'))['ingresos_totales__max']
        ingresos_totales_nomalized = 9 * ((float(self.ingresos_totales) - float(min_ingresos_totales)) / (float(max_ingresos_totales) - float(min_ingresos_totales))) + 1

        min_ingresos_ambiental_fiscales = IndicadorEconomico.objects.all().aggregate(Min('ingresos_ambiental_fiscales'))['ingresos_ambiental_fiscales__min']
        max_ingresos_ambiental_fiscales = IndicadorEconomico.objects.all().aggregate(Max('ingresos_ambiental_fiscales'))['ingresos_ambiental_fiscales__max']
        ingresos_ambiental_fiscales_nomalized = 9 * ((float(self.ingresos_ambiental_fiscales) - float(min_ingresos_ambiental_fiscales)) / (float(max_ingresos_ambiental_fiscales) - float(min_ingresos_ambiental_fiscales))) + 1


        min_ingresos_ambiental_preasignaciones = IndicadorEconomico.objects.all().aggregate(Min('ingresos_ambiental_preasignaciones'))['ingresos_ambiental_preasignaciones__min']
        max_ingresos_ambiental_preasignaciones = IndicadorEconomico.objects.all().aggregate(Max('ingresos_ambiental_preasignaciones'))['ingresos_ambiental_preasignaciones__max']
        ingresos_ambiental_preasignaciones_nomalized = 9 * ((float(self.ingresos_ambiental_preasignaciones) - float(min_ingresos_ambiental_preasignaciones)) / (float(max_ingresos_ambiental_preasignaciones) - float(min_ingresos_ambiental_preasignaciones))) + 1

        min_ingresos_totales_ambiental = IndicadorEconomico.objects.all().aggregate(Min('ingresos_totales_ambiental'))['ingresos_totales_ambiental__min']
        max_ingresos_totales_ambiental = IndicadorEconomico.objects.all().aggregate(Max('ingresos_totales_ambiental'))['ingresos_totales_ambiental__max']
        ingresos_totales_ambiental_nomalized = 9 * ((float(self.ingresos_totales_ambiental) - float(min_ingresos_totales_ambiental)) / (float(max_ingresos_totales_ambiental) - float(min_ingresos_ambiental_preasignaciones))) + 1

        self.subindice = (presupuesto_normalized + monto_residencial_normalized + monto_industrial_nomalized +ingresos_fiscales_nomalized + ingresos_preasignaciones_nomalized +ingresos_asistencia_nomalized + ingresos_credito_nomalized + ingresos_anticipos_nomalized + ingresos_totales_nomalized + ingresos_ambiental_fiscales_nomalized + ingresos_ambiental_preasignaciones_nomalized + ingresos_totales_ambiental_nomalized) / 12  # Promedio de todas las variables normalizadas
        self.save()



class IndicadorInstitucional(models.Model):
    id_institucional = models.AutoField(primary_key=True)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    anio = models.IntegerField(default=2020)
    funcionarios_tiempo_completo = models.IntegerField()
    cobertura_km_barrido_publicas = models.DecimalField(max_digits=12, decimal_places=2)
    personas_servicio_barrido =  models.IntegerField()
    personas_gestion_ambiental =  models.IntegerField()
    energia_kWh = models.DecimalField(max_digits=12, decimal_places=2)
    energia_valor = models.DecimalField(max_digits=12, decimal_places=2)
    combustible_diesel = models.DecimalField(max_digits=12, decimal_places=2)
    combustible_extra = models.DecimalField(max_digits=12, decimal_places=2)
    combustible_super = models.DecimalField(max_digits=12, decimal_places=2)
    num_productos =  models.IntegerField()
    num_cortes_servicio =  models.IntegerField()
    subindice = models.DecimalField(max_digits=12, decimal_places=2)

    def calculate_subindice(self):
        min_funcionarios = IndicadorInstitucional.objects.all().aggregate(Min('funcionarios_tiempo_completo'))['funcionarios_tiempo_completo__min']
        max_funcionarios = IndicadorInstitucional.objects.all().aggregate(Max('funcionarios_tiempo_completo'))['funcionarios_tiempo_completo__max']
        funcionarios_normalized = 9 * ((float(self.funcionarios_tiempo_completo) - min_funcionarios) / (max_funcionarios - min_funcionarios)) + 1

        min_cobertura = IndicadorInstitucional.objects.all().aggregate(Min('cobertura_km_barrido_publicas'))['cobertura_km_barrido_publicas__min']
        max_cobertura = IndicadorInstitucional.objects.all().aggregate(Max('cobertura_km_barrido_publicas'))['cobertura_km_barrido_publicas__max']
        cobertura_normalized = 9 * ((float(self.cobertura_km_barrido_publicas) - float(min_cobertura)) / ( float(max_cobertura) - float(min_cobertura))) + 1

        min_personas_servicio_barrido = IndicadorInstitucional.objects.all().aggregate(Min('personas_servicio_barrido'))['personas_servicio_barrido__min']
        max_personas_servicio_barrido = IndicadorInstitucional.objects.all().aggregate(Max('personas_servicio_barrido'))['personas_servicio_barrido__max']
        persona_barrido_nomalized = 9 * ((float(self.personas_servicio_barrido) - float(min_personas_servicio_barrido)) / (float(max_personas_servicio_barrido) - float(min_personas_servicio_barrido))) + 1

        min_personas_ambiental = IndicadorInstitucional.objects.all().aggregate(Min('personas_gestion_ambiental'))['personas_gestion_ambiental__min']
        max_personas_ambiental = IndicadorInstitucional.objects.all().aggregate(Max('personas_gestion_ambiental'))['personas_gestion_ambiental__max']
        persona_ambiental_nomalized = 9 * ((float(self.personas_gestion_ambiental) - float(min_personas_ambiental)) / (float(max_personas_ambiental) - float(min_personas_ambiental))) + 1

        min_energia_kWh = IndicadorInstitucional.objects.all().aggregate(Min('energia_kWh'))['energia_kWh__min']
        max_energia_kWh = IndicadorInstitucional.objects.all().aggregate(Max('energia_kWh'))['energia_kWh__max']
        energia_kwh_nomalized = 9 * ((float(self.energia_kWh) - float(min_energia_kWh)) / (float(max_energia_kWh) - float(min_energia_kWh))) + 1

        min_energia_valor = IndicadorInstitucional.objects.all().aggregate(Min('energia_valor'))['energia_valor__min']
        max_energia_valor = IndicadorInstitucional.objects.all().aggregate(Max('energia_valor'))['energia_valor__max']
        energia_valor_nomalized = 9 * ((float(self.energia_valor) - float(min_energia_valor)) / (float(max_energia_valor) - float(min_energia_valor))) + 1

        min_combustible_diesel = IndicadorInstitucional.objects.all().aggregate(Min('combustible_diesel'))['combustible_diesel__min']
        max_combustible_diesel = IndicadorInstitucional.objects.all().aggregate(Max('combustible_diesel'))['combustible_diesel__max']
        diesel_nomalized = 9 * ((float(self.combustible_diesel) - float(min_combustible_diesel)) / (float(max_combustible_diesel) - float(min_combustible_diesel))) + 1

        min_combustible_extra = IndicadorInstitucional.objects.all().aggregate(Min('combustible_extra'))['combustible_extra__min']
        max_combustible_extra = IndicadorInstitucional.objects.all().aggregate(Max('combustible_extra'))['combustible_extra__max']
        extra_nomalized = 9 * ((float(self.combustible_extra) - float(min_combustible_extra)) / (float(max_combustible_extra) - float(min_combustible_extra))) + 1

        min_combustible_super = IndicadorInstitucional.objects.all().aggregate(Min('combustible_super'))['combustible_super__min']
        max_combustible_super = IndicadorInstitucional.objects.all().aggregate(Max('combustible_super'))['combustible_super__max']
        super_nomalized = 9 * ((float(self.combustible_super) - float(min_combustible_super)) / (float(max_combustible_super) - float(min_combustible_super))) + 1

        min_num_productos = IndicadorInstitucional.objects.all().aggregate(Min('num_productos'))['num_productos__min']
        max_num_productos = IndicadorInstitucional.objects.all().aggregate(Max('num_productos'))['num_productos__max']
        productos_nomalized = 9 * ((float(self.num_productos) - float(min_num_productos)) / (float(max_num_productos) - float(min_num_productos))) + 1


        min_num_cortes_servicio = IndicadorInstitucional.objects.all().aggregate(Min('num_cortes_servicio'))['num_cortes_servicio__min']
        max_num_cortes_servicio = IndicadorInstitucional.objects.all().aggregate(Max('num_cortes_servicio'))['num_cortes_servicio__max']
        servico_nomalized = 9 * ((float(self.num_cortes_servicio) - float(min_num_cortes_servicio)) / (float(max_num_cortes_servicio) - float(min_num_cortes_servicio))) + 1

        self.subindice = (funcionarios_normalized + cobertura_normalized + persona_barrido_nomalized +persona_ambiental_nomalized + energia_kwh_nomalized +energia_valor_nomalized + diesel_nomalized + extra_nomalized + super_nomalized + productos_nomalized + servico_nomalized) / 11  # Promedio de todas las variables normalizadas
        self.save()
        # variables = [
        #     self.funcionarios_tiempo_completo,
        #     self.cobertura_km_barrido_publicas,
        #     self.personas_servicio_barrido,
        #     self.personas_gestion_ambiental,
        #     self.energia_kWh,
        #     self.energia_valor,
        #     self.combustible_diesel,
        #     self.combustible_extra,
        #     self.combustible_super,
        #     self.num_productos,
        #     self.num_cortes_servicio
        # ]   
        
    
        # variable_min = min(variables)
        # variable_max = max(variables)
        # subindice = 0
        # for variable in variables:
        #     if variable_max - variable_min == 0:
        #         continue
        #     # print(variable - variable_min)
        #     # print(variable_max - variable_min)
        #     subindice += (9 * ((float(variable) - variable_min) / (variable_max - variable_min))) + 1
        #     print(subindice)

        # # print(len(variables))
        # subindice =  subindice / len(variables)
        # self.subindice = subindice
        # print(self.municipio.nombre)
        # print(f"El subíndice es: {subindice}")
        # self.save()
    





class IndicadorSocial(models.Model):
    id_social = models.AutoField(primary_key=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    anio = models.IntegerField(default=2020)
    num_vehiculos = models.IntegerField()
    capacidad_tone_vehiculos = models.IntegerField()
    porcentaje_barrido = models.IntegerField()
    km_barrido = models.DecimalField(max_digits=12, decimal_places=2)
    porcentaje_barrido_urbanas = models.IntegerField()
    porcentaje_barrido_rurales = models.IntegerField()
    porcentaje_residuos = models.IntegerField()
    proyectos_conservacion_agua = models.IntegerField()
    abast_agua_horas =models.IntegerField()
    area_m2_institucion = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_parques = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_plazas = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_jardines = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_parterres = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_riberas = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_estadios = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_canchas = models.DecimalField(max_digits=12, decimal_places=2)
    area_m2_urbanas = models.DecimalField(max_digits=12, decimal_places=2)
    area_total_hect = models.DecimalField(max_digits=12, decimal_places=2)
    subindice = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    
    def calculate_subindice(self):

        min_num_vehiculos = IndicadorSocial.objects.all().aggregate(Min('num_vehiculos'))['num_vehiculos__min']
        max_num_vehiculos = IndicadorSocial.objects.all().aggregate(Max('num_vehiculos'))['num_vehiculos__max']
        num_vehiculos_normalized = 9 * ((float(self.num_vehiculos) - float(min_num_vehiculos)) / ( float(max_num_vehiculos) - float(min_num_vehiculos))) + 1

        min_capacidad_tone_vehiculos = IndicadorSocial.objects.all().aggregate(Min('capacidad_tone_vehiculos'))['capacidad_tone_vehiculos__min']
        max_capacidad_tone_vehiculos = IndicadorSocial.objects.all().aggregate(Max('capacidad_tone_vehiculos'))['capacidad_tone_vehiculos__max']
        capacidad_tone_vehiculos_nomalized = 9 * ((float(self.capacidad_tone_vehiculos) - float(min_capacidad_tone_vehiculos)) / (float(max_capacidad_tone_vehiculos) - float(min_capacidad_tone_vehiculos))) + 1

        min_porcentaje_barrido = IndicadorSocial.objects.all().aggregate(Min('porcentaje_barrido'))['porcentaje_barrido__min']
        max_porcentaje_barrido = IndicadorSocial.objects.all().aggregate(Max('porcentaje_barrido'))['porcentaje_barrido__max']
        porcentaje_barrido_nomalized = 9 * ((float(self.porcentaje_barrido) - float(min_porcentaje_barrido)) / (float(max_porcentaje_barrido) - float(min_porcentaje_barrido))) + 1

        min_porcentaje_barrido_urbanas = IndicadorSocial.objects.all().aggregate(Min('porcentaje_barrido_urbanas'))['porcentaje_barrido_urbanas__min']
        max_porcentaje_barrido_urbanas = IndicadorSocial.objects.all().aggregate(Max('porcentaje_barrido_urbanas'))['porcentaje_barrido_urbanas__max']
        porcentaje_barrido_urbanas_nomalized = 9 * ((float(self.porcentaje_barrido_urbanas) - float(min_porcentaje_barrido_urbanas)) / (float(max_porcentaje_barrido_urbanas) - float(min_porcentaje_barrido_urbanas))) + 1

        min_porcentaje_barrido_rurales = IndicadorSocial.objects.all().aggregate(Min('porcentaje_barrido_rurales'))['porcentaje_barrido_rurales__min']
        max_porcentaje_barrido_rurales = IndicadorSocial.objects.all().aggregate(Max('porcentaje_barrido_rurales'))['porcentaje_barrido_rurales__max']
        porcentaje_barrido_rurales_nomalized = 9 * ((float(self.porcentaje_barrido_rurales) - float(min_porcentaje_barrido_rurales)) / (float(max_porcentaje_barrido_rurales) - float(min_porcentaje_barrido_rurales))) + 1

        min_porcentaje_residuos = IndicadorSocial.objects.all().aggregate(Min('porcentaje_residuos'))['porcentaje_residuos__min']
        max_porcentaje_residuos = IndicadorSocial.objects.all().aggregate(Max('porcentaje_residuos'))['porcentaje_residuos__max']
        porcentaje_residuos_nomalized = 9 * ((float(self.porcentaje_residuos) - float(min_porcentaje_residuos)) / (float(max_porcentaje_residuos) - float(min_porcentaje_residuos))) + 1

        min_proyectos_conservacion_agua = IndicadorSocial.objects.all().aggregate(Min('proyectos_conservacion_agua'))['proyectos_conservacion_agua__min']
        max_proyectos_conservacion_agua = IndicadorSocial.objects.all().aggregate(Max('proyectos_conservacion_agua'))['proyectos_conservacion_agua__max']
        proyectos_conservacion_agua_nomalized = 9 * ((float(self.proyectos_conservacion_agua) - float(min_proyectos_conservacion_agua)) / (float(max_proyectos_conservacion_agua) - float(min_proyectos_conservacion_agua))) + 1

        min_abast_agua_horas = IndicadorSocial.objects.all().aggregate(Min('abast_agua_horas'))['abast_agua_horas__min']
        max_abast_agua_horas = IndicadorSocial.objects.all().aggregate(Max('abast_agua_horas'))['abast_agua_horas__max']
        abast_agua_horas_nomalized = 9 * ((float(self.abast_agua_horas) - float(min_abast_agua_horas)) / (float(max_abast_agua_horas) - float(min_abast_agua_horas))) + 1

        min_area_m2_institucion = IndicadorSocial.objects.all().aggregate(Min('area_m2_institucion'))['area_m2_institucion__min']
        max_area_m2_institucion = IndicadorSocial.objects.all().aggregate(Max('area_m2_institucion'))['area_m2_institucion__max']
        area_m2_institucion_nomalized = 9 * ((float(self.area_m2_institucion) - float(min_area_m2_institucion)) / (float(max_area_m2_institucion) - float(min_area_m2_institucion))) + 1


        min_area_m2_parques = IndicadorSocial.objects.all().aggregate(Min('area_m2_parques'))['area_m2_parques__min']
        max_area_m2_parques = IndicadorSocial.objects.all().aggregate(Max('area_m2_parques'))['area_m2_parques__max']
        area_m2_parques_nomalized = 9 * ((float(self.area_m2_parques) - float(min_area_m2_parques)) / (float(max_area_m2_parques) - float(min_area_m2_parques))) + 1

        min_area_m2_plazas = IndicadorSocial.objects.all().aggregate(Min('area_m2_plazas'))['area_m2_plazas__min']
        max_area_m2_plazas = IndicadorSocial.objects.all().aggregate(Max('area_m2_plazas'))['area_m2_plazas__max']
        area_m2_plazas_nomalized = 9 * ((float(self.area_m2_plazas) - float(min_area_m2_plazas)) / (float(max_area_m2_plazas) - float(min_area_m2_plazas))) + 1

        min_area_m2_jardines = IndicadorSocial.objects.all().aggregate(Min('area_m2_jardines'))['area_m2_jardines__min']
        max_area_m2_jardines = IndicadorSocial.objects.all().aggregate(Max('area_m2_jardines'))['area_m2_jardines__max']
        area_m2_jardines_nomalized = 9 * ((float(self.area_m2_jardines) - float(min_area_m2_jardines)) / (float(max_area_m2_jardines) - float(min_area_m2_jardines))) + 1

        min_area_m2_parterres = IndicadorSocial.objects.all().aggregate(Min('area_m2_parterres'))['area_m2_parterres__min']
        max_area_m2_parterres = IndicadorSocial.objects.all().aggregate(Max('area_m2_parterres'))['area_m2_parterres__max']
        area_m2_parterres_nomalized = 9 * ((float(self.area_m2_parterres) - float(min_area_m2_parterres)) / (float(max_area_m2_parterres) - float(min_area_m2_parterres))) + 1

        min_area_m2_riberas = IndicadorSocial.objects.all().aggregate(Min('area_m2_riberas'))['area_m2_riberas__min']
        max_area_m2_riberas = IndicadorSocial.objects.all().aggregate(Max('area_m2_riberas'))['area_m2_riberas__max']
        area_m2_riberas_nomalized = 9 * ((float(self.area_m2_riberas) - float(min_area_m2_riberas)) / (float(max_area_m2_riberas) - float(min_area_m2_riberas))) + 1

        min_area_m2_estadios = IndicadorSocial.objects.all().aggregate(Min('area_m2_estadios'))['area_m2_estadios__min']
        max_area_m2_estadios = IndicadorSocial.objects.all().aggregate(Max('area_m2_estadios'))['area_m2_estadios__max']
        area_m2_estadios_nomalized = 9 * ((float(self.area_m2_estadios) - float(min_area_m2_estadios)) / (float(max_area_m2_estadios) - float(min_area_m2_estadios))) + 1

        min_area_m2_urbanas = IndicadorSocial.objects.all().aggregate(Min('area_m2_urbanas'))['area_m2_urbanas__min']
        max_area_m2_urbanas = IndicadorSocial.objects.all().aggregate(Max('area_m2_urbanas'))['area_m2_urbanas__max']
        area_m2_urbanas_nomalized = 9 * ((float(self.area_m2_urbanas) - float(min_area_m2_urbanas)) / (float(max_area_m2_urbanas) - float(min_area_m2_urbanas))) + 1

        min_area_m2_canchas = IndicadorSocial.objects.all().aggregate(Min('area_m2_canchas'))['area_m2_canchas__min']
        max_area_m2_canchas = IndicadorSocial.objects.all().aggregate(Max('area_m2_canchas'))['area_m2_canchas__max']
        area_m2_canchas_nomalized = 9 * ((float(self.area_m2_canchas) - float(min_area_m2_canchas)) / (float(max_area_m2_canchas) - float(min_area_m2_canchas))) + 1

        min_area_total_hect = IndicadorSocial.objects.all().aggregate(Min('area_total_hect'))['area_total_hect__min']
        max_area_total_hect = IndicadorSocial.objects.all().aggregate(Max('area_total_hect'))['area_total_hect__max']
        area_total_hect_nomalized = 9 * ((float(self.area_total_hect) - float(min_area_total_hect)) / (float(max_area_total_hect) - float(min_area_total_hect))) + 1

        self.subindice = (num_vehiculos_normalized + capacidad_tone_vehiculos_nomalized + porcentaje_barrido_nomalized +porcentaje_barrido_urbanas_nomalized + porcentaje_barrido_rurales_nomalized +proyectos_conservacion_agua_nomalized + abast_agua_horas_nomalized + area_m2_institucion_nomalized + area_m2_parques_nomalized + area_m2_plazas_nomalized + area_m2_jardines_nomalized + area_m2_parterres_nomalized + porcentaje_residuos_nomalized + area_m2_riberas_nomalized + area_m2_estadios_nomalized + area_m2_urbanas_nomalized + area_m2_canchas_nomalized + area_total_hect_nomalized) / 18  # Promedio de todas las variables normalizadas
        self.save()


class IndicadorAmbiental(models.Model):
    id_ambiental =models.AutoField(primary_key=True)
    municipio = models.ForeignKey('Municipio', on_delete=models.PROTECT)
    anio = models.IntegerField(default=2020)
    area_sanitarios = models.IntegerField()
    num_botaderos = models.IntegerField()
    area_botaderos =  models.IntegerField()
    total_residuos_tone = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_solidos = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_peligroso_ton = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_organicos_ton = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_inorganicos_ton = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos = models.DecimalField(max_digits=12, decimal_places=2)
    residuos_urbanos_reciclaje = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_urbanos = models.DecimalField(max_digits=12, decimal_places=2)
    total_residuos_solidos_peligrososo = models.DecimalField(max_digits=12, decimal_places=2)
    captacion_agua_superficial = models.DecimalField(max_digits=12, decimal_places=2)
    captacion_agua_subterranea = models.DecimalField(max_digits=12, decimal_places=2)
    volumen_total_superficial_subterranea = models.DecimalField(max_digits=12, decimal_places=2)
    volumen_bruto_dulce = models.DecimalField(max_digits=12, decimal_places=2)
    volumen_agua_usuario = models.DecimalField(max_digits=12, decimal_places=2)
    total_agua_residual_recolectada = models.DecimalField(max_digits=12, decimal_places=2)
    total_residual_tratamiento = models.DecimalField(max_digits=12, decimal_places=2)
    num_plantas_tratamiento_residual =  models.IntegerField()
    capacidad_tratamiento_residual = models.DecimalField(max_digits=12, decimal_places=2)
    total_agua_notratada_m3 = models.DecimalField(max_digits=12, decimal_places=2)
    total_agua_tratada_vertida = models.DecimalField(max_digits=12, decimal_places=2)
    total_agua_no_tratada_vertida = models.DecimalField(max_digits=12, decimal_places=2)
    catidad_agua_residual_alcatarillado_m3 = models.DecimalField(max_digits=12, decimal_places=2)
    consumo_agua = models.DecimalField(max_digits=12, decimal_places=2)
    subindice = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def calculate_subindice(self):

        min_area_sanitarios = IndicadorAmbiental.objects.all().aggregate(Min('area_sanitarios'))['area_sanitarios__min']
        max_area_sanitarios = IndicadorAmbiental.objects.all().aggregate(Max('area_sanitarios'))['area_sanitarios__max']
        area_sanitarios_normalized = 9 * ((float(self.area_sanitarios) - float(min_area_sanitarios)) / ( float(max_area_sanitarios) - float(min_area_sanitarios))) + 1

        min_num_botaderos = IndicadorAmbiental.objects.all().aggregate(Min('num_botaderos'))['num_botaderos__min']
        max_num_botaderos = IndicadorAmbiental.objects.all().aggregate(Max('num_botaderos'))['num_botaderos__max']
        num_botaderos_nomalized = 9 * ((float(self.num_botaderos) - float(min_num_botaderos)) / (float(max_num_botaderos) - float(min_num_botaderos))) + 1

        min_area_botaderos = IndicadorAmbiental.objects.all().aggregate(Min('area_botaderos'))['area_botaderos__min']
        max_area_botaderos = IndicadorAmbiental.objects.all().aggregate(Max('area_botaderos'))['area_botaderos__max']
        area_botaderos_nomalized = 9 * ((float(self.area_botaderos) - float(min_area_botaderos)) / (float(max_area_botaderos) - float(min_area_botaderos))) + 1

        min_total_residuos_tone = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_tone'))['total_residuos_tone__min']
        max_total_residuos_tone = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_tone'))['total_residuos_tone__max']
        total_residuos_tone_nomalized = 9 * ((float(self.total_residuos_tone) - float(min_total_residuos_tone)) / (float(max_total_residuos_tone) - float(min_total_residuos_tone))) + 1

        min_total_residuos_solidos = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_solidos'))['total_residuos_solidos__min']
        max_total_residuos_solidos = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_solidos'))['total_residuos_solidos__max']
        total_residuos_solidos_nomalized = 9 * ((float(self.total_residuos_solidos) - float(min_total_residuos_solidos)) / (float(max_total_residuos_solidos) - float(min_total_residuos_solidos))) + 1

        min_total_residuos_peligroso_ton = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_peligroso_ton'))['total_residuos_peligroso_ton__min']
        max_total_residuos_peligroso_ton = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_peligroso_ton'))['total_residuos_peligroso_ton__max']
        total_residuos_peligroso_ton_nomalized = 9 * ((float(self.total_residuos_peligroso_ton) - float(min_total_residuos_peligroso_ton)) / (float(max_total_residuos_peligroso_ton) - float(min_total_residuos_peligroso_ton))) + 1

        min_total_residuos_organicos_ton = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_organicos_ton'))['total_residuos_organicos_ton__min']
        max_total_residuos_organicos_ton = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_organicos_ton'))['total_residuos_organicos_ton__max']
        total_residuos_organicos_ton_nomalized = 9 * ((float(self.total_residuos_organicos_ton) - float(min_total_residuos_organicos_ton)) / (float(max_total_residuos_organicos_ton) - float(min_total_residuos_organicos_ton))) + 1

        min_total_residuos_inorganicos_ton = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_inorganicos_ton'))['total_residuos_inorganicos_ton__min']
        max_total_residuos_inorganicos_ton = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_inorganicos_ton'))['total_residuos_inorganicos_ton__max']
        total_residuos_inorganicos_ton_nomalized = 9 * ((float(self.total_residuos_inorganicos_ton) - float(min_total_residuos_inorganicos_ton)) / (float(max_total_residuos_inorganicos_ton) - float(min_total_residuos_inorganicos_ton))) + 1

        min_total_residuos = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos'))['total_residuos__min']
        max_total_residuos = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos'))['total_residuos__max']
        total_residuos_nomalized = 9 * ((float(self.total_residuos) - float(min_total_residuos)) / (float(max_total_residuos) - float(min_total_residuos))) + 1


        min_residuos_urbanos_reciclaje = IndicadorAmbiental.objects.all().aggregate(Min('residuos_urbanos_reciclaje'))['residuos_urbanos_reciclaje__min']
        max_residuos_urbanos_reciclaje = IndicadorAmbiental.objects.all().aggregate(Max('residuos_urbanos_reciclaje'))['residuos_urbanos_reciclaje__max']
        residuos_urbanos_reciclaje_nomalized = 9 * ((float(self.residuos_urbanos_reciclaje) - float(min_residuos_urbanos_reciclaje)) / (float(max_residuos_urbanos_reciclaje) - float(min_residuos_urbanos_reciclaje))) + 1

        min_total_residuos_urbanos = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_urbanos'))['total_residuos_urbanos__min']
        max_total_residuos_urbanos = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_urbanos'))['total_residuos_urbanos__max']
        total_residuos_urbanos_nomalized = 9 * ((float(self.total_residuos_urbanos) - float(min_total_residuos_urbanos)) / (float(max_total_residuos_urbanos) - float(min_total_residuos_urbanos))) + 1

        min_total_residuos_solidos_peligrososo = IndicadorAmbiental.objects.all().aggregate(Min('total_residuos_solidos_peligrososo'))['total_residuos_solidos_peligrososo__min']
        max_total_residuos_solidos_peligrososo = IndicadorAmbiental.objects.all().aggregate(Max('total_residuos_solidos_peligrososo'))['total_residuos_solidos_peligrososo__max']
        total_residuos_solidos_peligrososo_nomalized = 9 * ((float(self.total_residuos_solidos_peligrososo) - float(min_total_residuos_solidos_peligrososo)) / (float(max_total_residuos_solidos_peligrososo) - float(min_total_residuos_solidos_peligrososo))) + 1

        min_captacion_agua_superficial = IndicadorAmbiental.objects.all().aggregate(Min('captacion_agua_superficial'))['captacion_agua_superficial__min']
        max_captacion_agua_superficial = IndicadorAmbiental.objects.all().aggregate(Max('captacion_agua_superficial'))['captacion_agua_superficial__max']
        captacion_agua_superficial_nomalized = 9 * ((float(self.captacion_agua_superficial) - float(min_captacion_agua_superficial)) / (float(max_captacion_agua_superficial) - float(min_captacion_agua_superficial))) + 1

        min_captacion_agua_subterranea = IndicadorAmbiental.objects.all().aggregate(Min('captacion_agua_subterranea'))['captacion_agua_subterranea__min']
        max_captacion_agua_subterranea = IndicadorAmbiental.objects.all().aggregate(Max('captacion_agua_subterranea'))['captacion_agua_subterranea__max']
        captacion_agua_subterranea_nomalized = 9 * ((float(self.captacion_agua_subterranea) - float(min_captacion_agua_subterranea)) / (float(max_captacion_agua_subterranea) - float(min_captacion_agua_subterranea))) + 1

        min_volumen_total_superficial_subterranea = IndicadorAmbiental.objects.all().aggregate(Min('volumen_total_superficial_subterranea'))['volumen_total_superficial_subterranea__min']
        max_volumen_total_superficial_subterranea = IndicadorAmbiental.objects.all().aggregate(Max('volumen_total_superficial_subterranea'))['volumen_total_superficial_subterranea__max']
        volumen_total_superficial_subterranea_nomalized = 9 * ((float(self.volumen_total_superficial_subterranea) - float(min_volumen_total_superficial_subterranea)) / (float(max_volumen_total_superficial_subterranea) - float(min_volumen_total_superficial_subterranea))) + 1

        min_volumen_bruto_dulce = IndicadorAmbiental.objects.all().aggregate(Min('volumen_bruto_dulce'))['volumen_bruto_dulce__min']
        max_volumen_bruto_dulce = IndicadorAmbiental.objects.all().aggregate(Max('volumen_bruto_dulce'))['volumen_bruto_dulce__max']
        volumen_bruto_dulce_nomalized = 9 * ((float(self.volumen_bruto_dulce) - float(min_volumen_bruto_dulce)) / (float(max_volumen_bruto_dulce) - float(min_volumen_bruto_dulce))) + 1

        min_volumen_agua_usuario = IndicadorAmbiental.objects.all().aggregate(Min('volumen_agua_usuario'))['volumen_agua_usuario__min']
        max_volumen_agua_usuario = IndicadorAmbiental.objects.all().aggregate(Max('volumen_agua_usuario'))['volumen_agua_usuario__max']
        volumen_agua_usuario_nomalized = 9 * ((float(self.volumen_agua_usuario) - float(min_volumen_agua_usuario)) / (float(max_volumen_agua_usuario) - float(min_volumen_agua_usuario))) + 1

        min_total_agua_residual_recolectada = IndicadorAmbiental.objects.all().aggregate(Min('total_agua_residual_recolectada'))['total_agua_residual_recolectada__min']
        max_total_agua_residual_recolectada = IndicadorAmbiental.objects.all().aggregate(Max('total_agua_residual_recolectada'))['total_agua_residual_recolectada__max']
        total_agua_residual_recolectada_nomalized = 9 * ((float(self.total_agua_residual_recolectada) - float(min_total_agua_residual_recolectada)) / (float(max_total_agua_residual_recolectada) - float(min_total_agua_residual_recolectada))) + 1

        min_total_residual_tratamiento = IndicadorAmbiental.objects.all().aggregate(Min('total_residual_tratamiento'))['total_residual_tratamiento__min']
        max_total_residual_tratamiento = IndicadorAmbiental.objects.all().aggregate(Max('total_residual_tratamiento'))['total_residual_tratamiento__max']
        total_residual_tratamiento_nomalized = 9 * ((float(self.total_residual_tratamiento) - float(min_total_residual_tratamiento)) / (float(max_total_residual_tratamiento) - float(min_total_residual_tratamiento))) + 1

        min_num_plantas_tratamiento_residual = IndicadorAmbiental.objects.all().aggregate(Min('num_plantas_tratamiento_residual'))['num_plantas_tratamiento_residual__min']
        max_num_plantas_tratamiento_residual = IndicadorAmbiental.objects.all().aggregate(Max('num_plantas_tratamiento_residual'))['num_plantas_tratamiento_residual__max']
        num_plantas_tratamiento_residual_nomalized = 9 * ((float(self.num_plantas_tratamiento_residual) - float(min_num_plantas_tratamiento_residual)) / (float(max_num_plantas_tratamiento_residual) - float(min_num_plantas_tratamiento_residual))) + 1

        min_capacidad_tratamiento_residual = IndicadorAmbiental.objects.all().aggregate(Min('capacidad_tratamiento_residual'))['capacidad_tratamiento_residual__min']
        max_capacidad_tratamiento_residual = IndicadorAmbiental.objects.all().aggregate(Max('capacidad_tratamiento_residual'))['capacidad_tratamiento_residual__max']
        capacidad_tratamiento_residual_nomalized = 9 * ((float(self.capacidad_tratamiento_residual) - float(min_capacidad_tratamiento_residual)) / (float(max_capacidad_tratamiento_residual) - float(min_capacidad_tratamiento_residual))) + 1

        min_total_agua_notratada_m3 = IndicadorAmbiental.objects.all().aggregate(Min('total_agua_notratada_m3'))['total_agua_notratada_m3__min']
        max_total_agua_notratada_m3 = IndicadorAmbiental.objects.all().aggregate(Max('total_agua_notratada_m3'))['total_agua_notratada_m3__max']
        total_agua_notratada_m3_nomalized = 9 * ((float(self.total_agua_notratada_m3) - float(min_total_agua_notratada_m3)) / (float(max_total_agua_notratada_m3) - float(min_total_agua_notratada_m3))) + 1


        min_total_agua_tratada_vertida = IndicadorAmbiental.objects.all().aggregate(Min('total_agua_tratada_vertida'))['total_agua_tratada_vertida__min']
        max_total_agua_tratada_vertida = IndicadorAmbiental.objects.all().aggregate(Max('total_agua_tratada_vertida'))['total_agua_tratada_vertida__max']
        total_agua_tratada_vertida_nomalized = 9 * ((float(self.total_agua_tratada_vertida) - float(min_total_agua_tratada_vertida)) / (float(max_total_agua_tratada_vertida) - float(min_total_agua_tratada_vertida))) + 1


        min_total_agua_no_tratada_vertida = IndicadorAmbiental.objects.all().aggregate(Min('total_agua_no_tratada_vertida'))['total_agua_no_tratada_vertida__min']
        max_total_agua_no_tratada_vertida = IndicadorAmbiental.objects.all().aggregate(Max('total_agua_no_tratada_vertida'))['total_agua_no_tratada_vertida__max']
        total_agua_no_tratada_vertida_nomalized = 9 * ((float(self.total_agua_no_tratada_vertida) - float(min_total_agua_no_tratada_vertida)) / (float(max_total_agua_no_tratada_vertida) - float(min_total_agua_no_tratada_vertida))) + 1


        min_catidad_agua_residual_alcatarillado_m3 = IndicadorAmbiental.objects.all().aggregate(Min('catidad_agua_residual_alcatarillado_m3'))['catidad_agua_residual_alcatarillado_m3__min']
        max_catidad_agua_residual_alcatarillado_m3 = IndicadorAmbiental.objects.all().aggregate(Max('catidad_agua_residual_alcatarillado_m3'))['catidad_agua_residual_alcatarillado_m3__max']
        catidad_agua_residual_alcatarillado_m3_nomalized = 9 * ((float(self.catidad_agua_residual_alcatarillado_m3) - float(min_catidad_agua_residual_alcatarillado_m3)) / (float(max_catidad_agua_residual_alcatarillado_m3) - float(min_catidad_agua_residual_alcatarillado_m3))) + 1

        min_consumo_agua = IndicadorAmbiental.objects.all().aggregate(Min('consumo_agua'))['consumo_agua__min']
        max_consumo_agua = IndicadorAmbiental.objects.all().aggregate(Max('consumo_agua'))['consumo_agua__max']
        consumo_agua_nomalized = 9 * ((float(self.consumo_agua) - float(min_consumo_agua)) / (float(max_consumo_agua) - float(min_consumo_agua))) + 1



        self.subindice = (area_sanitarios_normalized + num_botaderos_nomalized + area_botaderos_nomalized +total_residuos_tone_nomalized + total_residuos_solidos_nomalized +total_residuos_peligroso_ton_nomalized + total_residuos_inorganicos_ton_nomalized + total_residuos_nomalized + captacion_agua_superficial_nomalized + total_residuos_urbanos_nomalized + total_residuos_solidos_peligrososo_nomalized + total_agua_residual_recolectada_nomalized + residuos_urbanos_reciclaje_nomalized + captacion_agua_subterranea_nomalized + volumen_total_superficial_subterranea_nomalized + volumen_bruto_dulce_nomalized + volumen_agua_usuario_nomalized + total_residual_tratamiento_nomalized + num_plantas_tratamiento_residual_nomalized + capacidad_tratamiento_residual_nomalized + total_agua_notratada_m3_nomalized + total_agua_tratada_vertida_nomalized + total_agua_no_tratada_vertida_nomalized + catidad_agua_residual_alcatarillado_m3_nomalized + consumo_agua_nomalized + total_residuos_organicos_ton_nomalized) / 25  # Promedio de todas las variables normalizadas
        self.save()
