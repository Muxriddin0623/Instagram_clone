from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=True, primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
