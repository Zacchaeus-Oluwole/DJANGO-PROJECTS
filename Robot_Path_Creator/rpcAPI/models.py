from django.db import models

# Create your models here.


class Path(models.Model):
    direction = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def json_object(self):
        return {
            'direction': self.direction,
            'created': self.created
        }

    def __str__(self):
        return self.direction


class Destination(models.Model):
    name = models.CharField(max_length=250)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
