# Generated by Django 3.2.9 on 2021-12-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_autor_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='Red social/website'),
        ),
    ]
