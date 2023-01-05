# from django.db import models
# from django.conf import settings


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     date_of_birth = models.DateField(blank=True, null=True)
#     photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

#     def __str__(self):
#         return f'Profile for user {self.user.username}'


from django.db import models

# Create your models here.

class Perpetrator(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    offence = models.CharField(max_length=250)

    class Meta:
        db_table = "perpetrator"