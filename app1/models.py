from django.db import models


choices = (
    ('local','local'),
    ('outside  ujjain','outside  ujjain'),
)


class AppUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="Asset/images")
    category = models.CharField(max_length=32,choices=choices)

    def __str__(self):
        return self.name