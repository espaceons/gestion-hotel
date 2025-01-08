from django.db import models

# Create your models here.

class Room(models.Model):
    nom = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    etat = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
