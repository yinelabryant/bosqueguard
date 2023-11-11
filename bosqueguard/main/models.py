from django.db import models

# Create your models here.
class EvaluacionAmbiental(models.Model):
    PuntajeSeccion1 = models.FloatField()
    PuntajeSeccion2 = models.FloatField()
    PuntajeSeccion3 = models.FloatField()
    PuntajeSeccion4 = models.FloatField()
    PuntajeSeccion5 = models.FloatField()
    PuntajeSeccion6 = models.FloatField()
    PuntajeSeccion7 = models.FloatField()
    PuntajeSeccion8 = models.FloatField()
    PuntajeSeccion9 = models.FloatField()
    PuntajeSeccion10 = models.FloatField()
    PuntajeSeccion11 = models.FloatField()
    PuntajeSeccion12 = models.FloatField()
    PuntajeSeccion13 = models.FloatField()
    PuntajeSeccion14 = models.FloatField()
    PuntajeTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Evaluación Ambiental #{self.id}'