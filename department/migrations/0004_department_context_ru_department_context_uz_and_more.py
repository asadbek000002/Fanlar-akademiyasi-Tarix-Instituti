# Generated by Django 5.0.1 on 2024-01-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_alter_category_options_category_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='context_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='context_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bio_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='degree_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='degree_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fullname_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fullname_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='research',
            name='context_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='research',
            name='context_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='works',
            name='works_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='works',
            name='works_uz',
            field=models.TextField(null=True),
        ),
    ]