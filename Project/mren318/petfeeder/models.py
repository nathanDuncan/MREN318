from typing import Any
from django.db import models
from . import LEDs
# Create your models here.

class Pet(models.Model):
    # Input parameters
    name = models.CharField(max_length=50)
    servingSize = models.PositiveSmallIntegerField()
    servingsPerDay = models.PositiveSmallIntegerField()

    # Output Parameters
    consumptionToday = models.PositiveSmallIntegerField()
    visitationsToday = models.PositiveSmallIntegerField()
    avgTimeAtFeeder = models.PositiveSmallIntegerField()

    # Functions
    # Feednow()

    def __str__(self):
        return self.name

    def Feednow(self):
        if self.servingsPerDay == 3:
            LEDs.LED_Blink()


