from django.db import models
import uuid


class ProjectModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=280)
    stack = models.JSONField(default=list)
    thumbnail = models.CharField(max_length=40)
    slug = models.CharField(max_length=40, default='/')

    def __str__(self):
        return str(self.name)

