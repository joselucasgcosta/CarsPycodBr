from django.contrib import admin
from cars.models import Car, Brand, Serie


class BrandAdmin(admin.ModelAdmin):
    """ Cria uma classe para gerenciar o modelo Brand"""
    list_display = ('name',)
    search_fields = ('name',)


class SerieAdmin(admin.ModelAdmin):
    """ Cria uma classe para gerenciar o modelo Series"""
    list_display = ('serie',)
    search_fields = ('serie',)


class CarAdmin(admin.ModelAdmin):
    """ Cria uma classe para gerenciar o modelo Car"""
    list_display = ('model', 'brand', 'serie', 'factory_year',
                    'model_year', 'value')
    search_fields = ('model', 'brand', 'serie')


# Registra que as classes
admin.site.register(Brand, BrandAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Car, CarAdmin)
