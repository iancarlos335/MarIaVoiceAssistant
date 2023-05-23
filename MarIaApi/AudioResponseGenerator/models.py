from django.db import models


# Create your models here.
class IaAudioResponse(models.Model):
    AudioId = models.AutoField(primary_key=True)
    AudioBinaryContent = models.BinaryField()
    AudioStringContent = models.CharField(max_length=255, default='')
