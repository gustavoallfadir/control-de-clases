from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from registro_clases.models import Clase 

# Create your models here.

class Maestro(models.Model):

    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = PhoneField(blank=True)
    email = models.EmailField(blank=True)
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    nacimiento = models.DateField(
        blank=True,
        null=True,
        verbose_name='fecha de nacimiento')
    foto = models.ImageField(
        blank=True,
        upload_to='maestros',
    )
    horas_contrato = models.IntegerField(default=100)
    es_admin = models.BooleanField(default=False)

    def clases_este_mes(self):
        ano_actual = timezone.now().year
        mes_actual = timezone.now().month
        clases_este_mes = Clase.objects.filter(
            maestro=self.pk).filter(
                fecha__year=ano_actual).filter(
                    fecha__month=mes_actual).count()
        return clases_este_mes


    def horas_este_mes(self):
        ano_actual = timezone.now().year
        mes_actual = timezone.now().month
        clases_este_mes = Clase.objects.all().filter(maestro=self.pk)\
            .filter(aprobada=True)\
                .filter(fecha__year=ano_actual)\
                    .filter(fecha__month=mes_actual)\
                        .values_list('duracion', flat=True)
        horas = 0
        for x in clases_este_mes:
           horas = horas+x
        return horas

    def ultimas_clases(self):
        ultimas_clases = Clase.objects.filter(maestro=self.pk).order_by('-fecha')[:10]
        return ultimas_clases


    def total_clases(self):
        total_clases = Clase.objects.filter(maestro=self.pk)\
            .filter(rechazada=False).count()
        return total_clases


    def clases_pendientes(self):
        clases_pendientes = Clase.objects.filter(maestro=self.pk)\
            .filter(aprobada=False)\
                .filter(rechazada=False)

        return clases_pendientes


    def total_pendientes(self):
        total_pendientes = Clase.objects.filter(maestro=self.pk).filter(aprobada=False).filter(rechazada=False).count()
        return total_pendientes

    def __str__(self):
        return '%s %s' %(self.nombres,self.apellidos)

    class Meta:
        verbose_name = 'maestro'
        verbose_name_plural = 'maestros'


    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Maestro.objects.create(usuario=instance)
            instance.maestro.save()

