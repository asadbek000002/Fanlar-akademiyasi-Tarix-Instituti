# Generated by Django 5.0.1 on 2024-01-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_contact', '0002_partnerorganizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalprojects',
            name='project_status',
            field=models.CharField(choices=[('done', 'done'), ('not_done', 'not_done')], default='bajarilmagan', max_length=20),
        ),
    ]
