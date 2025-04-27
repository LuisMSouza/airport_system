from django.db import models

class Airports(models.Model):
    table_name = 'airports'
    """
    Model representing an airport.
    """

    id = models.AutoField(primary_key=True)
    iata = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.iata} - {self.city}, {self.state}"

    class Meta:
        db_table = 'airports'