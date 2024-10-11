from django.contrib import admin
from .models import pagina_inicial
<<<<<<< HEAD

# Register your models here.

admin.site.register(pagina_inicial)
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

# Register your models here.

admin.site.register(pagina_inicial)

admin.site.register(plagas_y_enfermedades)

admin.site.register(etapa_de_crecimiento)

admin.site.register(etapa_de_plantacion)

admin.site.register(etapa_de_fructificacion)

admin.site.register(etapa_de_floracion)

admin.site.register(consejos_para_su_cultivo)

admin.site.register(seleccion_semilla)

admin.site.register(cuidado_inicial)

admin.site.register(sembrado)

admin.site.register(fertilizacion)
>>>>>>> 7fd819e (definicion del perfil)
