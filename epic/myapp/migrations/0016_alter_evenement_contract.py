# Generated by Django 4.0.4 on 2022-05-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_contract_event_evenement_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.contract'),
        ),
    ]