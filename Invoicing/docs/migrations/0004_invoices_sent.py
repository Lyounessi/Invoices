# Generated by Django 3.2 on 2021-04-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_alter_invoices_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]