# Generated by Django 5.0.1 on 2024-01-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category_lib', 'verbose_name_plural': 'Categories_lib'},
        ),
        migrations.AddField(
            model_name='archive',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='archive',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='autoreferat',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='autoreferat',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='degree_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='degree_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='fullname_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='fullname_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='ish_joyi_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='ish_joyi_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='degree_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='degree_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='fullname_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='fullname_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='ish_joyi_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='editorialmany',
            name='ish_joyi_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='electronbook',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='electronbook',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='context',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirement',
            name='context_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='context_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
