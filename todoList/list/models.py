from django.db import models

# Create your models here.
class Lista(models.Model):
    description = models.CharField('description',max_length=100, blank=False)
    status = models.BooleanField('status', blank=False)
    creation_date = models.DateField('Fecha alta',null=False)

    def __str__(self) -> str:
        return f"Description: {self.description} Status: {str(self.status)} Creation Date:{str(self.creation_date)}" 