# Generated by Django 5.1.4 on 2025-03-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariocustomizado',
            name='tipo_sanguineo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
