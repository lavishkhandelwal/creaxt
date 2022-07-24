from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class topic(models.Model):
    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name_plural = "Topic"

    def __str__(self):
        return self.slug