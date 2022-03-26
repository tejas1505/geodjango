from django.db import models

class city(models.Model):
    name = models.CharField(max_length=25)
    latitude=models.CharField(max_length=10,null=True)
    longitude=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'