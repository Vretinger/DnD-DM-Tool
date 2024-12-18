# Generated by Django 5.1.2 on 2024-10-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersheets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='charactersheet',
            old_name='equipment',
            new_name='notes',
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='charisma',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='constitution',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='dexterity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='intelligence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='level',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='charactersheet',
            name='spells',
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='strength',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersheet',
            name='wisdom',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='inventory',
            field=models.ManyToManyField(blank=True, to='charactersheets.item'),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='skills',
            field=models.ManyToManyField(blank=True, to='charactersheets.skill'),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='spells',
            field=models.ManyToManyField(blank=True, to='charactersheets.spell'),
        ),
    ]
