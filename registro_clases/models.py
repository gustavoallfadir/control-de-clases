from django.db import models

# Create your models here.

class Asignatura(models.Model):
    "Clase modelo para asignaturas"

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'asignatura'
        verbose_name_plural = 'asignaturas'


class TipoClase(models.Model):
    "Clase modelo para tipos de clase"
    
    nombre = models.CharField(max_length=30)
    tabulador = models.DecimalField(
        default=1,
        verbose_name='tabulador de pago',
        max_digits=4,
        decimal_places=2,
    )
    
    class meta:
        verbose_name = 'tipo de clase'
        verbose_name_plural = 'tipos de clase'
    
    def __str__(self):
        return self.nombre


class Clase(models.Model):

    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    tipo = models.ForeignKey(
        TipoClase,
        on_delete=models.CASCADE, 
        verbose_name='tipo de clase',
        blank=True,
        null=True,
    )
    maestro = models.ForeignKey(to='maestros.maestro',on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.DecimalField(
        default=1,
        max_digits=3,
        decimal_places=1,
        verbose_name='duración de la clase en horas',
    )
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

    def estatus(self):
        estatus = 'Pendiente'
        if self.aprobada == True:
            estatus = 'Aprobada'
        elif self.rechazada == True:
            estatus = 'Rechazada'
        return estatus
    
    def fue_rechazada(self):
        return self.rechazada