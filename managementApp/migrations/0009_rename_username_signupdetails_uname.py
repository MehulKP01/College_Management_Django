# Generated by Django 4.2.1 on 2024-03-01 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementApp', '0008_signupdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdetails',
            old_name='username',
            new_name='uname',
        ),
    ]
