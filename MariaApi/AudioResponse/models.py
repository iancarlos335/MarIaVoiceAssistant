from django.db import models


# Create your models here.

class IaAudioResponse(models.Model):
    id = models.AutoField(primary_key=True)
    binaryContent = models.BinaryField()
    stringResponse = models.CharField(max_length=255, default="")
