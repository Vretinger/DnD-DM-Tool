from django import forms
from .models import CharacterSheet

class CharacterSheetForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = ['name', 'race', 'character_class', 'walking_speed', 'level', 'strength', 'dexterity',
                  'constitution', 'intelligence', 'wisdom', 'charisma', 'inventory', 'spells', 'heroic_inspiration']
