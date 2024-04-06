
from django.db import models

class ExtractionSchema(models.Model):
    name = models.CharField(max_length=200)
    schema = models.JSONField()

    def __str__(self):
        return self.name
