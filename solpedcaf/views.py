from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import pagina_inicial
<<<<<<< HEAD
=======
from .models import plagas_y_enfermedades
from .models import etapa_de_crecimiento
from .models import etapa_de_plantacion
from .models import etapa_de_fructificacion
from .models import etapa_de_floracion
from .models import consejos_para_su_cultivo
from .models import seleccion_semilla
from .models import cuidado_inicial
from .models import sembrado
from .models import fertilizacion
>>>>>>> 7fd819e (definicion del perfil)
from .forms import RegistroForm, LoginForm

# Vista para listar objetos de la modelo 'pagina_inicial'
def pagina_inicial_list(request):
    pagina_inicials = pagina_inicial.objects.all()
    return render(request, 'pagina_inicial/post/list.html', {'pagina_inicials': pagina_inicials})

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'pagina_inicial/registro.html', {'form': form})

# Vista para el inicio de sesión
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
<<<<<<< HEAD
            return redirect('pagina_inicial_list')  # Redirige a la lista después de iniciar sesión
=======
            if user.is_superuser:
                return redirect('admin/admin.site.urls')  # Redirige al panel de admin
            else:
                return redirect('pagina_inicial_list')  # Redirige a la vista de usuario
>>>>>>> 7fd819e (definicion del perfil)
    else:
        form = LoginForm()
    return render(request, 'pagina_inicial/login.html', {'form': form})

# Vista para cerrar sesión
@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

# Vista para la página inicial protegida
@login_required
def pagina_inicial_view(request):
    return render(request, 'pagina_inicial/pagina_inicial.html', {'user': request.user})


<<<<<<< HEAD
=======
#vista para la pagina plagas y enfermedades 

def plagas_y_enfermedades_list(request):
    plagas_y_enfermedadess = plagas_y_enfermedades.objects.all()
    return render(
        request,
        'plagas_y_enfermedades/post/list.html', {'plagas_y_enfermedadess': plagas_y_enfermedadess})


#vista para etapa de crecimiento del modulo plagas y enfermedades

def etapa_de_crecimiento_list(request):
    etapa_de_crecimientos = etapa_de_crecimiento.objects.all()
    return render(
        request,
        'plagas_y_enfermedades/etapa_de_crecimiento/post/list.html', {'etapa_de_crecimientos': etapa_de_crecimientos}
    )

#vista para etapa de plantacion del modulo plagas y enfermedades

def etapa_de_plantacion_list(request):
    etapa_de_plantacions = etapa_de_plantacion.objects.all()
    return render(
        request,
        'plagas_y_enfermedades/etapa_de_plantacion/post/list.html', {'etapa_de_plantacions': etapa_de_plantacions}
    )


#vista para etapa de fructificacion del modulo plagas y enfermedades

def etapa_de_fructificacion_list(request):
    etapa_de_fructificacions = etapa_de_fructificacion.objects.all()
    return render(
        request,
        'plagas_y_enfermedades/etapa_de_fructificacion/post/list.html', {'etapa_de_fructificacions': etapa_de_fructificacions}
    )

#vista para etapa de floracion del modulo plagas y enfermedades

def etapa_de_floracion_list(request):
    etapa_de_floracions = etapa_de_floracion.objects.all()
    return render(
        request,
        'plagas_y_enfermedades/etapa_de_floracion/post/list.html', {'etapa_de_floracions': etapa_de_floracions}
    )


#vista para consejos para su cultivo

def consejos_para_su_cultivo_list(request):
    consejos_para_su_cultivos = consejos_para_su_cultivo.objects.all()
    return render(
        request,
        'consejos_para_su_cultivo/post/list.html', {'consejos_para_su_cultivos': consejos_para_su_cultivos}
    )


#vista para seleccion semilla de consejos para su cultivo

def seleccion_semilla_list(request):
    seleccion_semillas = seleccion_semilla.objects.all()
    return render(
        request,
        'consejos_para_su_cultivo/seleccion_semilla/post/list.html', {'seleccion_semillas': seleccion_semillas}
    )

#vista para cuidado inicial de consejos para su cultivo

def cuidado_inicial_list(request):
    cuidado_inicials = cuidado_inicial.objects.all()
    return render(
        request,
        'consejos_para_su_cultivo/cuidado_inicial/post/list.html', {'cuidado_inicials': cuidado_inicials}
    )


#vistas para sembrado de consejos para su cultivo 

def sembrado_list(request):
    sembrados = sembrado.objects.all()
    return render(
        request,
        'consejos_para_su_cultivo/sembrado/post/list.html', {'sembrados': sembrados}
    )


#vistas para fertilizacion de consejos para su cultivo 

def fertilizacion_list(request):
    fertilizacions = fertilizacion.objects.all()
    return render(
        request,
        'consejos_para_su_cultivo/fertilizacion/post/list.html', {'fertilizacions': fertilizacions}
    )

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

@login_required
def editar_perfil(request):
    user = request.user

    if user.is_superuser:
        return redirect('admin:index')  # Redirigir al panel de administración

    perfil, created = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Actualiza el usuario
        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        user.save()

        # Actualiza el perfil
        perfil.phone = phone
        perfil.save()

        return redirect('pagina_inicial_list')  # Redirigir después de guardar

    return render(request, 'pagina_inicial.html', {'perfil': perfil})

# Señales para manejar la creación y actualización de perfiles
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Solo crea perfil si no es superusuario
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'perfil'):
        instance.perfil.save()

from django.contrib.auth.decorators import user_passes_test

def is_not_superuser(user):
    return not user.is_superuser

@login_required
@user_passes_test(is_not_superuser)
def pagina_inicial_view(request):
    return render(request, 'pagina_inicial/pagina_inicial.html', {'user': request.user})

#seguridad 
>>>>>>> 7fd819e (definicion del perfil)
