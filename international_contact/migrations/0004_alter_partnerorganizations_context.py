# Generated by Django 5.0.1 on 2024-01-25 09:33

import djrichtextfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('international_contact', '0003_alter_internationalprojects_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerorganizations',
            name='context',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
