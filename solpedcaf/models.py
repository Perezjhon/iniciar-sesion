from django.db import models

# Create your models here.

#PAGINA INICIAL MODELS

class pagina_inicial(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    urlDestino = models.CharField(max_length=200, null=True)


    def __str__(self):
<<<<<<< HEAD
        return self.titulo
=======
        return self.titulo
    
#PLAGA Y ENFERMEDADES MODELS 

class plagas_y_enfermedades(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    urlDestino = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.titulo

#PLAGAS Y ENFERMEDADES ETAPA CRECIMIENTO MODELS 

class etapa_de_crecimiento(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)



    def __str__(self):
        return self.titulo


#PLAGAS Y ENFERMEDADES ETAPA PLANTACION MODELS 

class etapa_de_plantacion(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)



    def __str__(self):
        return self.titulo
    

#PLAGAS Y ENFERMEDADES ETAPA FRUCTIFICACION MODELS 

class etapa_de_fructificacion(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)



    def __str__(self):
        return self.titulo


#PLAGAS Y ENFERMEDADES ETAPA FLORACION MODELS 

class etapa_de_floracion(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)



    def __str__(self):
        return self.titulo




#CONSEJOS PARA SU CULTIVO MODELS

class consejos_para_su_cultivo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    urlDestino = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.titulo



#CONSEJOS PARA SU CULTIVO SELECCION SEMILLA MODELS

class seleccion_semilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    a_tener_en_cuenta = models.TextField( null=True)
    a_tener_en_cuenta2 = models.TextField( null=True)
    a_tener_en_cuenta3 = models.TextField(null=True)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)


    def __str__(self):
        return self.nombre




#CONSEJOS PARA SU CULTIVO CUIDADO INICIAL MODELS 

class cuidado_inicial(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    a_tener_en_cuenta = models.TextField( null=True, blank=True)
    a_tener_en_cuenta2 = models.TextField( null=True, blank=True)
    a_tener_en_cuenta3 = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    


    def __str__(self):
        return self.nombre



#CONSEJOS PARA SU CULTIVO SEMBRADO MODELS 

class sembrado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    a_tener_en_cuenta = models.TextField( null=True, blank=True)
    a_tener_en_cuenta2 = models.TextField( null=True, blank=True)
    a_tener_en_cuenta3 = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    


    def __str__(self):
        return self.nombre
    


#CONSEJOS PARA SU CULTIVO FERTILIZACION MODELS 

class fertilizacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    a_tener_en_cuenta = models.TextField( null=True, blank=True)
    a_tener_en_cuenta2 = models.TextField( null=True, blank=True)
    a_tener_en_cuenta3 = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='modulos', null=True, blank=True)
    


    def __str__(self):
        return self.nombre


#user perfil

from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otra_info = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
>>>>>>> 7fd819e (definicion del perfil)
