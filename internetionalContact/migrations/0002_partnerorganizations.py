# Generated by Django 5.0.1 on 2024-01-22 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetionalContact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerOrganizations',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internetionalContact.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/internetionalContact/partner_organizations')),
                ('context', models.TextField()),
            ],
            bases=('internetionalContact.basemodel',),
        ),
    ]
