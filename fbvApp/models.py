from django.db import models

# Create your models here.
class Passenger(models.Model):
  id = models.IntegerField(primary_key=True)
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  travel_points = models.DecimalField(max_digits=10,decimal_places=2)
  
  def __str__(self):
    return self.id + self.first_name + self.last_name, self.travel_points