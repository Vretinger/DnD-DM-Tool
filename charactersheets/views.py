from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import CharacterSheet
from .forms import CharacterSheetForm
import math


# Function to calculate proficiency bonus based on character level
def get_proficiency_bonus(level):
    if level >= 1 and level <= 4:
        return 2
    elif level >= 5 and level <= 8:
        return 3
    elif level >= 9 and level <= 12:
        return 4
    elif level >= 13 and level <= 16:
        return 5
    elif level >= 17 and level <= 20:
        return 6
    else:
        return 0  # Return 0 if level is out of range for safety


def home(request):
    return render(request, 'charactersheets/home.html')


# View for listing character sheets (only user's own sheets)
@login_required
def character_sheet_list(request):
    sheets = CharacterSheet.objects.filter(user=request.user)
    return render(request, 'charactersheets/character_sheet_list.html', {'sheets': sheets})


def calculate_proficiency_bonus(level):
    # Example logic: proficiency bonus increases every 4 levels
    return 2 + (level - 1) // 4


# View for displaying a specific character sheet
@login_required
def character_sheet_detail(request, pk):
    character = get_object_or_404(CharacterSheet, pk=pk)

    # Calculate base modifiers
    modifiers = {
        'strength': (character.strength - 10) // 2,
        'dexterity': (character.dexterity - 10) // 2,
        'constitution': (character.constitution - 10) // 2,
        'intelligence': (character.intelligence - 10) // 2,
        'wisdom': (character.wisdom - 10) // 2,
        'charisma': (character.charisma - 10) // 2,
    }

    proficiency_bonus = calculate_proficiency_bonus(character.level)

    # Skill list with proficiency application (example structure)
    skills = [
    {"name": "Acrobatics", "abbr": "DEX", "modifier": modifiers['dexterity'], "bonus": proficiency_bonus if character.proficient_in_acrobatics else 0},
    {"name": "Animal Handling", "abbr": "WIS", "modifier": modifiers['wisdom'], "bonus": proficiency_bonus if character.proficient_in_animal_handling else 0},
    {"name": "Arcana", "abbr": "INT", "modifier": modifiers['intelligence'], "bonus": proficiency_bonus if character.proficient_in_arcana else 0},
    {"name": "Athletics", "abbr": "STR", "modifier": modifiers['strength'], "bonus": proficiency_bonus if character.proficient_in_athletics else 0},
    {"name": "Deception", "abbr": "CHA", "modifier": modifiers['charisma'], "bonus": proficiency_bonus if character.proficient_in_deception else 0},
    {"name": "History", "abbr": "INT", "modifier": modifiers['intelligence'], "bonus": proficiency_bonus if character.proficient_in_history else 0},
    {"name": "Insight", "abbr": "WIS", "modifier": modifiers['wisdom'], "bonus": proficiency_bonus if character.proficient_in_insight else 0},
    {"name": "Intimidation", "abbr": "CHA", "modifier": modifiers['charisma'], "bonus": proficiency_bonus if character.proficient_in_intimidation else 0},
    {"name": "Investigation", "abbr": "INT", "modifier": modifiers['intelligence'], "bonus": proficiency_bonus if character.proficient_in_investigation else 0},
    {"name": "Medicine", "abbr": "WIS", "modifier": modifiers['wisdom'], "bonus": proficiency_bonus if character.proficient_in_medicine else 0},
    {"name": "Nature", "abbr": "INT", "modifier": modifiers['intelligence'], "bonus": proficiency_bonus if character.proficient_in_nature else 0},
    {"name": "Perception", "abbr": "WIS", "modifier": modifiers['wisdom'], "bonus": proficiency_bonus if character.proficient_in_perception else 0},
    {"name": "Performance", "abbr": "CHA", "modifier": modifiers['charisma'], "bonus": proficiency_bonus if character.proficient_in_performance else 0},
    {"name": "Persuasion", "abbr": "CHA", "modifier": modifiers['charisma'], "bonus": proficiency_bonus if character.proficient_in_persuasion else 0},
    {"name": "Religion", "abbr": "INT", "modifier": modifiers['intelligence'], "bonus": proficiency_bonus if character.proficient_in_religion else 0},
    {"name": "Sleight of Hand", "abbr": "DEX", "modifier": modifiers['dexterity'], "bonus": proficiency_bonus if character.proficient_in_sleight_of_hand else 0},
    {"name": "Stealth", "abbr": "DEX", "modifier": modifiers['dexterity'], "bonus": proficiency_bonus if character.proficient_in_stealth else 0},
    {"name": "Survival", "abbr": "WIS", "modifier": modifiers['wisdom'], "bonus": proficiency_bonus if character.proficient_in_survival else 0},
    ]


    context = {
        'character': character,
        'skills': skills,
        'strength_modifier': modifiers['strength'],
        'dexterity_modifier': modifiers['dexterity'],
        'constitution_modifier': modifiers['constitution'],
        'intelligence_modifier': modifiers['intelligence'],
        'wisdom_modifier': modifiers['wisdom'],
        'charisma_modifier': modifiers['charisma'],
        'proficiency_bonus': proficiency_bonus,
    }

    return render(request, 'charactersheets/character_sheet_detail.html', context)

@require_POST
@login_required
def update_health(request, pk):
    character = get_object_or_404(CharacterSheet, pk=pk)
    
    if 'heal' in request.POST:
        health_modifier_amount = int(request.POST.get('health_modifier_amount', 0))
        character.current_health = min(character.current_health + health_modifier_amount, character.max_health)
    
    elif 'damage' in request.POST:
        health_modifier_amount = int(request.POST.get('health_modifier_amount', 0))
        character.current_health = max(character.current_health - health_modifier_amount, 0)
    
    character.save()
    return redirect('character_sheet_detail', pk=pk)

# View for creating a new character sheet
@login_required
def character_sheet_create(request):
    if request.method == 'POST':
        form = CharacterSheetForm(request.POST)
        if form.is_valid():
            character_sheet = form.save(commit=False)
            character_sheet.user = request.user
            character_sheet.save()
            return redirect('character_sheet_detail', pk=character_sheet.pk)
    else:
        form = CharacterSheetForm()
    return render(request, 'charactersheets/character_sheet_form.html', {'form': form})

# View for editing an existing character sheet
@login_required
def character_sheet_edit(request, pk):
    sheet = get_object_or_404(CharacterSheet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CharacterSheetForm(request.POST, instance=sheet)
        if form.is_valid():
            form.save()
            return redirect('character_sheet_detail', pk=sheet.pk)
    else:
        form = CharacterSheetForm(instance=sheet)
    return render(request, 'charactersheets/character_sheet_form.html', {'form': form})
