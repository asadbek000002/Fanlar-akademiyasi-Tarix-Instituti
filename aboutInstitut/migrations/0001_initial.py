# Generated by Django 5.0.1 on 2024-01-20 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArchitecturalLegalDocuments',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('context', models.TextField()),
            ],
            options={
                'verbose_name': 'Architectural Legal Document',
                'verbose_name_plural': 'Architectural Legal Documents',
            },
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='HistoryInstitute',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/aboutInstitut/history_institute')),
                ('contex', models.TextField()),
            ],
            options={
                'verbose_name': 'History Institute',
                'verbose_name_plural': 'History Institutes',
            },
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('position', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('reception_days', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/aboutInstitut/leadership')),
            ],
            options={
                'verbose_name': 'Leadership',
                'verbose_name_plural': 'Leaderships',
            },
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/aboutInstitut/news')),
                ('context', models.TextField()),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='OrganizationStructure',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('image', models.ImageField(upload_to='images/aboutInstitut/organization_structure')),
            ],
            options={
                'verbose_name': 'Organization Structure',
                'verbose_name_plural': 'Organization Structures',
            },
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='HistoryInstituteImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('history_institute_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_institute_img', to='aboutInstitut.historyinstitute')),
            ],
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='LeadershipImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('leadership_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leadership_img', to='aboutInstitut.leadership')),
            ],
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('news_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_img', to='aboutInstitut.news')),
            ],
            bases=('aboutInstitut.basemodel',),
        ),
        migrations.CreateModel(
            name='OrganizationStructureImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aboutInstitut.basemodel')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('organization_structure_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_structure_img', to='aboutInstitut.organizationstructure')),
            ],
            bases=('aboutInstitut.basemodel',),
        ),
    ]
