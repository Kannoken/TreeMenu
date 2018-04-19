from django.db import models

class FooModel(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255, default='')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.DO_NOTHING)
# Create your models here.
