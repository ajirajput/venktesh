# Generated by Django 3.1.2 on 2021-02-02 15:53

import datetime
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('modified_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile_no', models.CharField(max_length=10)),
                ('subject', models.CharField(default='', max_length=150)),
                ('message', models.TextField(default='')),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('modified_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('icon', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail_image', models.ImageField(blank=True, max_length=150, null=True, upload_to='services/')),
                ('short_content', models.TextField()),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('modified_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('category', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='website.category')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServiceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('long_content', models.TextField()),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('modified_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='website.service')),
            ],
            options={
                'verbose_name': 'Service Detail',
                'verbose_name_plural': 'Service Details',
            },
        ),
        migrations.CreateModel(
            name='GalleryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(max_length=150, upload_to='gallery/')),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('modified_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='website.gallery')),
            ],
            options={
                'verbose_name': 'Gallery Details',
                'verbose_name_plural': 'Gallery Details',
            },
        ),
    ]
