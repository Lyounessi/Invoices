# Generated by Django 2.2 on 2020-12-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sellPrice',
            field=models.DecimalField(decimal_places=10, default=2000, max_digits=19),
            preserve_default=False,
        ),
    ]
