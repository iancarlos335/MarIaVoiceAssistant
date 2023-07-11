from django.db import models
from django.utils.timezone import datetime
import uuid
import os

# Create your models here.


def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    created_at = models.DateField(auto_now=True)

class IaResponse(models.Model):
    question = models.CharField(max_length=255)
    audio_responses = models.FileField(upload_to=get_upload_path)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    date_register = models.DateTimeField(default=datetime.now())