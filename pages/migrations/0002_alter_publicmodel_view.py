# Generated by Django 4.1.5 on 2023-03-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicmodel',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
