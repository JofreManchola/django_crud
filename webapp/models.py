from django.db import models

from django.contrib.auth.models import User, Group

# Create your models here.


class Evento(models.Model):

    CONFERENCIA = 'CF'
    SEMINARIO = 'SE'
    CONGRESO = 'CG'
    CURSO = 'CU'
    PRESENCIAL = 'PR'
    VIRTUAL = 'VI'

    CATEGORIA_CHOICES = (
        (CONFERENCIA, 'Conferencia'),
        (SEMINARIO, 'Seminario'),
        (CONGRESO, 'Congreso'),
        (CURSO, 'Curso')
    )

    TIPO_CHOICES = (
        (PRESENCIAL, 'Presencial'),
        (VIRTUAL, 'Virtual')
    )

    nombre = models.CharField(
        max_length=1000, help_text='Nombre del evento', verbose_name='Nombre')
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, help_text='Categoría del evento', verbose_name='Categoría')
    lugar = models.CharField(
        max_length=1000, help_text='Lugar donde se realizará el evento', verbose_name='Lugar')
    direccion = models.CharField(
        max_length=1000, help_text='Dirección donde se realizará el evento', verbose_name='Dirección')
    fecha_inicio = models.DateTimeField(
        help_text='Fecha y hora de inicio del evento', verbose_name='Fecha de inicio')
    fecha_fin = models.DateTimeField(
        help_text='Fecha y hora de finalización del evento', verbose_name='Fecha de finalización')
    tipo = models.CharField(
        max_length=20, choices=TIPO_CHOICES, help_text='Tipo del evento: Presencial o virtual', verbose_name='Tipo')
    # userId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        tmpTipo = [item[1]
                   for item in self.CATEGORIA_CHOICES if item[0] == self.CONFERENCIA][0]
        return self.nombre + ' (' + tmpTipo + ')'

    def __unicode__(self):
        return self.nombre
