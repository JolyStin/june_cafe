from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position', )


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField(blank=True)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('category', 'position', )


class Booking(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    phone_regex = RegexValidator(
        regex=r'^(\+38)?0\d{9}$',
        message='Phone number must be entered in the format: +380xxxxxxxxx, 0xxxxxxxxx',
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200, blank=True)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.date}'

    class Meta:
        ordering = ('-date_in', )


class MainMenuItem(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}/{self.slug}'

    def get_absolute_url(self):
        return reverse('home') + f'#{self.slug}'

    class Meta:
        ordering = ('position', )

class Contact(models.Models):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    phone_regex = RegexValidator(
        regex=r'^(\+38)?0\d{9}$',
        message='Phone number must be entered in the format: +380xxxxxxxxx, 0xxxxxxxxx',
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    message = models.TextField(max_length=200, blank=True)









