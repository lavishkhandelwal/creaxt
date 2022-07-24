from django.db import models
from django.contrib.auth.models import User
from Topic.models import topic

class post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
    topic = models.ForeignKey(topic, on_delete=models.CASCADE, related_name = 'post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title
    