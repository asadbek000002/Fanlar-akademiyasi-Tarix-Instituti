# Generated by Django 5.0.1 on 2024-01-24 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_options_alter_research_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category_dep', 'verbose_name_plural': 'categories_dep'},
        ),
    ]
