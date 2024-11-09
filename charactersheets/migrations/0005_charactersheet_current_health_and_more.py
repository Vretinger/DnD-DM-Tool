# Generated by Django 5.1.2 on 2024-10-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersheets', '0004_charactersheet_max_health'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='current_health',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='temp_health',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='max_health',
            field=models.IntegerField(default=0),
        ),
    ]