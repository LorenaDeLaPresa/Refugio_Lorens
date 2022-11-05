# Generated by Django 4.1.2 on 2022-11-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('clase_animal', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='posts')),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_blog', models.CharField(max_length=15)),
                ('titulo_blog', models.CharField(max_length=35)),
                ('subtitulo_blog', models.CharField(max_length=45)),
                ('creado_por', models.CharField(max_length=45)),
            ],
        ),
    ]
