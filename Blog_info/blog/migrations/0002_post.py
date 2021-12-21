# Generated by Django 4.0 on 2021-12-20 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=120, verbose_name='Descripción')),
                ('imagen', models.ImageField(null=True, upload_to='', verbose_name='Imagen')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categorias')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posteos',
            },
        ),
    ]