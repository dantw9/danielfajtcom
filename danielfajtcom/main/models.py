from django.db import models
import uuid


class DailyQuoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quote_id = models.CharField(max_length=40)
    quote = models.CharField(max_length=600)
    author = models.CharField(max_length=40)
    permalink = models.CharField(max_length=40, blank=True)
    copyright = models.CharField(max_length=80, blank=True)
    xxx = models.BinaryField

    def __str__(self):
        return str(self.quote)


class DailyBackgroundModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bg_id = models.CharField(max_length=40)
    bg_author = models.CharField(max_length=40)
    bg_url = models.CharField(max_length=80)
    bg_str_b64 = models.TextField(max_length=400000)

    def __str__(self):
        return str(self.bg_url)