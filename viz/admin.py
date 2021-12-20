from django.contrib import admin

# Register your models here.

from .models import Move, Species, Item, Ability

admin.site.register(Move)
admin.site.register(Species)
admin.site.register(Item)
admin.site.register(Ability)
