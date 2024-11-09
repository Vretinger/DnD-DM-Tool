# charactersheets/models.py
from django.contrib.auth.models import User
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

class Spell(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

class CharacterSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    max_health = models.IntegerField(default=0)
    current_health = models.IntegerField(default=0)
    temp_health = models.IntegerField(default=0)
    walking_speed = models.IntegerField(default=30)
    level = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    charisma = models.IntegerField()
    wisdom = models.IntegerField()
    intelligence = models.IntegerField()
    constitution = models.IntegerField()
    skills = models.ManyToManyField(Skill, blank=True)  # Relationship for skills
    inventory = models.ManyToManyField(Item, blank=True)  # Relationship for inventory
    spells = models.ManyToManyField(Spell, blank=True)  # Relationship for spells
    notes = models.TextField(blank=True)
    heroic_inspiration = models.IntegerField(default=0)
    proficient_in_acrobatics = models.BooleanField(default=False)
    proficient_in_animal_handling = models.BooleanField(default=False)
    proficient_in_arcana = models.BooleanField(default=False)
    proficient_in_athletics = models.BooleanField(default=False)
    proficient_in_deception = models.BooleanField(default=False)
    proficient_in_history = models.BooleanField(default=False)
    proficient_in_insight = models.BooleanField(default=False)
    proficient_in_intimidation = models.BooleanField(default=False)
    proficient_in_investigation = models.BooleanField(default=False)
    proficient_in_medicine = models.BooleanField(default=False)
    proficient_in_nature = models.BooleanField(default=False)
    proficient_in_perception = models.BooleanField(default=False)
    proficient_in_performance = models.BooleanField(default=False)
    proficient_in_persuasion = models.BooleanField(default=False)
    proficient_in_religion = models.BooleanField(default=False)
    proficient_in_sleight_of_hand = models.BooleanField(default=False)
    proficient_in_stealth = models.BooleanField(default=False)
    proficient_in_survival = models.BooleanField(default=False)

    def __str__(self):
        return self.name
