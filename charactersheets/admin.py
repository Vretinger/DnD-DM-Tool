from django.contrib import admin
from .models import CharacterSheet


class CharacterSheetAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'character_class', 'level']
    search_fields = ['name', 'user__username', 'character_class']

admin.site.register(CharacterSheet, CharacterSheetAdmin)
