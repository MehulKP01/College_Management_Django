# Generated by Django 4.2.1 on 2024-02-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=20)),
                ('unumber', models.CharField(max_length=11)),
                ('uemail', models.CharField(max_length=20)),
                ('umessage', models.TextField()),
            ],
        ),
    ]
