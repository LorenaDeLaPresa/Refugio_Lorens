# Generated by Django 4.1.2 on 2022-11-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_animal_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]