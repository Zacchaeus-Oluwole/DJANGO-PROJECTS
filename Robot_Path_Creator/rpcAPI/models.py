from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=250)

    # def json_object(self):
    #     return {
    #         'name': self.name,
    #     }
    
    def __str__(self):
        return self.name

class Path(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='direction', null=True)
    path = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)

    # def json_object(self):
    #     return {
    #         'destination': self.destination,
    #         'path': self.path,
    #         'created': self.created
    #     }

    def __str__(self):
        return str(self.destination)
