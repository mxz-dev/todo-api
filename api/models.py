from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Todo(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE, )
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task} - {self.author}'
    
    class Meta:
        verbose_name_plural = 'todo'