from django.db import models

# Create your models here.

class Dataset(models.Model):
    cca_section = models.CharField(max_length=5)
    offence = models.TextField()
    law = models.TextField()
    penalty = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.offence

    # class Meta:
    #     db_table = "dataset"