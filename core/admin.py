from django.contrib import admin
from .models import shortURL

class shortUrlAdmin(admin.ModelAdmin):
    list_display=['key','url']
admin.site.register(shortURL,shortUrlAdmin)


# Register your models here.
