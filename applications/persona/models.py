from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Registros Habilidades'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 



JOB_CHOICES = (
    ('0', 'CONTADOR'),
    ('1', 'ADMINISTRADOR'),
    ('2', 'ECONOMISTA'),
    ('3', 'OTRO'),
)

class Empleado(models.Model):
    """ Modelo para tabla empleado """
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres Completos', 
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departameto = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField('Imagen', upload_to=None, blank=True, height_field=None, width_field=None, max_length=None, null=True)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
 
    class Meta:
        verbose_name = 'Registros de Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['last_name']    # ['-name'] orden inverso
        #unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name # + '-' + self.job + '-' + self.departameto