# Generated by Django 4.0.5 on 2022-07-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0005_alter_exercise_time_alter_workout_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='time',
            field=models.TextField(blank=True, null=True),
        ),
    ]