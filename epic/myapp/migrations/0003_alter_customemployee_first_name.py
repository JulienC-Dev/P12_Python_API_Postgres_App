# Generated by Django 4.0.4 on 2022-05-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customemployee_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customemployee',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]