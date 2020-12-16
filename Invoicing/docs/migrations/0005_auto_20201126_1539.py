# Generated by Django 2.2 on 2020-11-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20201126_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='number',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]