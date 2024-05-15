from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class PriceType(models.TextChoices):
    EURO = 'EURO', 'EURO'
    DOLLAR = '$', '$'
    SUM = 'SO`M', 'SO`M'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    number = models.IntegerField()
    duration = models.DateField()
    taken = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='media/product')
    price_type = models.CharField(max_length=50, choices=PriceType.choices)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(max_length=1, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/profile')
    address = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rating = models.FloatField(max_length=1, default=0)
    comment = models.TextField()
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/client')
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]
