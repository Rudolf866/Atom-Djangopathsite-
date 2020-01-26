from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):# будет выдавать не объект класса Articles,а заголовок наших статей в админке
        return self.title
