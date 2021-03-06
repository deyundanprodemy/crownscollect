# Generated by Django 3.0.8 on 2020-08-01 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrownsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(max_length=200, null=True)),
                ('Slug', models.SlugField(max_length=500, unique=True)),
                ('Updated_on', models.DateTimeField(auto_now=True)),
                ('Description', models.TextField(blank=True)),
                ('Created_on', models.DateTimeField(auto_now_add=True)),
                ('Status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish to Home'), (2, 'Publish to Male wears'), (3, 'Publish to female wears'), (4, 'Publish to T-Shirts'), (5, 'Publish to Joggers'), (6, 'Publish to Trousers'), (7, 'Publish to Gowns'), (8, 'Publish to Hoods'), (9, 'Publish to Vintages'), (10, 'Publish to foot wears')], default=0)),
                ('Socials', models.CharField(max_length=500)),
                ('Mobile', models.CharField(max_length=500)),
                ('Price', models.CharField(blank=True, max_length=20)),
                ('Pic1', models.ImageField(blank=True, upload_to='')),
                ('Pic2', models.ImageField(blank=True, upload_to='')),
                ('Pic3', models.ImageField(blank=True, upload_to='')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NNH', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Created_on'],
            },
        ),
    ]
