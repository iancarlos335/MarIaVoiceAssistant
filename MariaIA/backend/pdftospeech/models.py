from django.db import models

import os
import uuid


def get_upload_path(instance, filename):
    return os.path.join(str(instance.uid), filename)


# Create your models here.
class Pdf(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now=True)
