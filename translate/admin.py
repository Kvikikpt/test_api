from django.contrib import admin
from .models import Translate

# Register your models here.


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    pass
