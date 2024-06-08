# Generated by Django 4.2.1 on 2024-02-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementApp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admissioninfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sfname', models.CharField(max_length=20)),
                ('smname', models.CharField(max_length=20)),
                ('smail', models.CharField(max_length=20)),
                ('snumber', models.CharField(max_length=20)),
                ('scity', models.CharField(max_length=20)),
                ('sstate', models.CharField(max_length=20)),
                ('sdistrict', models.CharField(max_length=20)),
                ('sdob', models.DateField()),
                ('saadhar', models.CharField(max_length=20)),
                ('seducation', models.CharField(max_length=20)),
                ('sphoto', models.ImageField(upload_to='managementApp/image/')),
                ('scategory', models.CharField(max_length=20)),
                ('sgender', models.CharField(max_length=20)),
                ('scourse', models.CharField(max_length=20)),
            ],
        ),
    ]
