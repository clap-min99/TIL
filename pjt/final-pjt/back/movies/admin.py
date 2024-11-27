from django.contrib import admin

# Register your models here.
from .models import Beer, BeerImage, Whiskey, WhiskeyImage, Wine, WineImage, NonAlcohol, NonAlcoholImage

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('subtype', 'description')

@admin.register(BeerImage)
class BeerImageAdmin(admin.ModelAdmin):
    list_display = ('beer', 'description', 'image')

@admin.register(Whiskey)
class WhiskeyAdmin(admin.ModelAdmin):
    list_display = ('subtype', 'description')

@admin.register(WhiskeyImage)
class WhiskeyImageAdmin(admin.ModelAdmin):
    list_display = ('whiskey', 'description', 'image')

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('subtype', 'description')

@admin.register(WineImage)
class WineImageAdmin(admin.ModelAdmin):
    list_display = ('wine', 'description', 'image')

@admin.register(NonAlcohol)
class NonAlcoholAdmin(admin.ModelAdmin):
    list_display = ('subtype', 'description')

@admin.register(NonAlcoholImage)
class NonAlcoholImageAdmin(admin.ModelAdmin):
    list_display = ('nonalcohol', 'description', 'image')