# Generated by Django 2.2 on 2020-12-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0017_auto_20201222_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='fnb',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
