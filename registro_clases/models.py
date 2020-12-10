from django.db import models

# Create your models here.

class Asignatura(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'asignatura'
        verbose_name_plural = 'asignaturas'


class Clase(models.Model):

    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    maestro = models.ForeignKey(to='maestros.maestro',on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    aprobada = models.BooleanField(default=False, verbose_name='aprobada para pago')
    rechazada = models.BooleanField(default=False, verbose_name='rechazada')

    def __str__(self):
        return 'clase de %s, impartida por %s el %s a las %s' %(
            self.asignatura,
            self.maestro,
            self.fecha.strftime('%d/%b/%y'),
            self.hora.strftime('%H:%M')
            )

    class meta:
        verbose_name = 'clase'
        verbose_name_plural = 'clases'

    def descripcion_corta(self):
        return 'Clase de %s, el %s a las %s' %(
            self.asignatura,
            self.fecha.strftime('%d de %b'),
            self.hora.strftime('%H:%M')
            )