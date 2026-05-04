from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'sensor_data'
        managed = False # Impede que o Django tente criar ou modificar a tabela no banco de dados