# Generated by Django 4.2.1 on 2024-03-01 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementApp', '0006_alter_admissioninfo_sphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissioninfo',
            name='sphoto',
        ),
    ]
