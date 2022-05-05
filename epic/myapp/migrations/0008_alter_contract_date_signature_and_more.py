# Generated by Django 4.0.4 on 2022-05-05 14:20

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_evenement_localisation_evenement_ville'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_signature',
            field=models.DateTimeField(blank=True, null=True, validators=[myapp.models.date_check]),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='date_event_begin',
            field=models.DateTimeField(blank=True, null=True, validators=[myapp.models.date_check]),
        ),
    ]