from django.contrib import admin
from .models import DishCategory, Dish, Booking
from .models import MainMenuItem

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Booking)


@admin.register(MainMenuItem)
class MainMenuItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
