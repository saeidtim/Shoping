# Generated by Django 4.1.5 on 2023-03-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default=1, upload_to='avatar/'),
            preserve_default=False,
        ),
    ]
