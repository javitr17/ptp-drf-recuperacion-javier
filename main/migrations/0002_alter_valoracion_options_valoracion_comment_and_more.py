# Generated by Django 5.0.6 on 2024-06-10 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valoracion',
            options={'verbose_name_plural': 'Valoraciones'},
        ),
        migrations.AddField(
            model_name='valoracion',
            name='comment',
            field=models.TextField(default='hola mundo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valoracion',
            name='fecha_registro',
            field=models.DateTimeField(default='2023-07-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valoracion',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valoracion',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valoracion',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
