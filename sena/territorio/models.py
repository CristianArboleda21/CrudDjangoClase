from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Monitoria(models.Model):
    cat = models.CharField(max_length=100)
    aprendiz = models.ForeignKey(Aprendiz, on_delete = models.DO_NOTHING)
    fecha_Inicio = models.DateTimeField()
    fecha_Final = models.DateTimeField() 

    def __str__(self):
        return f"{self.aprendiz} - {self.cat}"

class Actividades(models.Model):
    monitor = models.ForeignKey(Monitoria, on_delete=models.DO_NOTHING)
    actividad_Realizada = models.CharField(max_length=100)
    obs = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.actividad_Realizada