# Generated by Django 5.0.7 on 2024-08-21 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_spec', models.CharField(max_length=255)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departments')),
            ],
        ),
    ]
