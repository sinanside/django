from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=120,verbose_name="Başlık")
    content=models.TextField(verbose_name="İçerik")
    publiishing_date=models.DateTimeField(verbose_name="Yayınlanma tarihi")

    def __str__(self):
        return self.title


