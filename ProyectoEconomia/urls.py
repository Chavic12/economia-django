
from django.contrib import admin
from django.urls import path
from economia import views
from django.contrib.auth import views as auth_views
from usuarios.views import loginUsuario, logoutUsuario, RegistroUsuario
from django.contrib.auth.decorators import login_required
from economia.views import mostrar_subindice



# from usuario.views import views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', login_required(views.quienes), name="inicio"),
    path('contactos/', login_required(views.contactos), name='contactos'),
    path('tipoCalculo/', login_required(views.tipoCalculo), name='tipoCalculo'),
    path('upload/', login_required(views.upload), name='upload'),
    # path('indicadores/', login_required(views.indicadores), name='indicadores'),
    path('quienes/', login_required(views.quienes), name='quienes'),

    path('', views.home, name="inicio"),
    # TODO: Formularios
    path('ambiental/', views.agregar_indicador_ambiental, name='ambiental'),
    path('economico/', views.agregar_indicador_economico, name='economico'),
    path('institucional/', views.agregar_indicador_institucional, name='institucional'),
    path('social/', views.agregar_indicador_social, name='social'),
    path('guardar_formulario_ambiental/', views.guardar_formulario_ambiental, name='guardar_formulario_ambiental'),

    # path('mostrar_subindice/', views.mostrar_subindice, name='select_municipality'),
    path('seleccion_municipio/', views.seleccion_municipio, name='seleccion_municipio'),
    path('grafico_municipios/', views.grafico_municipios, name='grafico_municipios'),
    # TODO: LOGIN Y REGISTER
    path('logout/',login_required(logoutUsuario),name='logout'),
    path('accounts/login/',loginUsuario.as_view(), name='login'),
    path('register/', RegistroUsuario.as_view(), name="registro"),    

    # Conexión de url de olvido contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="auth/resetpswd.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="auth/resetconfirmpswd.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    

    
]
