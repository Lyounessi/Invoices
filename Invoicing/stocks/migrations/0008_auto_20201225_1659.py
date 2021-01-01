# Generated by Django 2.2 on 2020-12-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_auto_20201225_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='buyPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='gainMargin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='sellPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]