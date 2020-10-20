from django.contrib import admin
from .models import game, clothes, top

# Register your models here.
class gameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class clothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class clothesTop(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(game, gameAdmin)
admin.site.register(clothes, clothesAdmin)
admin.site.register(top, clothesTop)