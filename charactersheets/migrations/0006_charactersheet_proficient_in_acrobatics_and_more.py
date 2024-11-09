# Generated by Django 5.1.2 on 2024-10-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersheets', '0005_charactersheet_current_health_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_acrobatics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_animal_handling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_arcana',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_athletics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_deception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_history',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_insight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_intimidation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_investigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_medicine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_nature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_perception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_performance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_persuasion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_religion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_sleight_of_hand',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_stealth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='proficient_in_survival',
            field=models.BooleanField(default=False),
        ),
    ]
