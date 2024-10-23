from django.db import models
from django.contrib.auth.models import User

class CharacterSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    equipment = models.TextField(blank=True)
    spells = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.character_class} (Lvl {self.level})'
