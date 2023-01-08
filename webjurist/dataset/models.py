from django.db import models

# Create your models here.

class Dataset(models.Model):
    cca_section = models.CharField(max_length=10)
    offence = models.TextField()
    law = models.TextField()
    penalty = models.TextField()

    def __str__(self) -> str:
        return self.offence

    # class Meta:
    #     db_table = "dataset"