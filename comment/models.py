from django.db import models
from django.contrib.auth.models import User
from post.models import post

# Create your models here.
class comment(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()    
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name = 'comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comment"

    def __str__(self):
        return self.title