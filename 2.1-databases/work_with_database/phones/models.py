from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateTimeField()
    lte_exist = models.BooleanField()
    slug = models.SlugField()
