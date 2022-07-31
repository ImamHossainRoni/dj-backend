from django.db import models

# Create your models here.
from django.db import models
import uuid


class ActiveManager(models.Manager):
    """ Only returns active objects"""

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class InactiveManager(models.Manager):
    """ Only returns inactive objects"""

    def get_queryset(self):
        return super().get_queryset().filter(active=False)


class BaseModel(models.Model):
    """
    Used in all the models as base
    """
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True,
                                 blank=True,
                                 help_text='If this object is active')

    active_objects = ActiveManager()
    inactive_objects = InactiveManager()
    objects = models.Manager()

    class Meta:
        abstract = True
