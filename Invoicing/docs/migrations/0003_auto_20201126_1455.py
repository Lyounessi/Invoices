# Generated by Django 2.2 on 2020-11-26 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_auto_20201126_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='client',
            field=models.ForeignKey(choices=[('pyd', 'payed'), ('npyd', 'notPayed'), ('cnl', 'canceled')], default='npyd', on_delete=django.db.models.deletion.CASCADE, to='clients.Clients'),
        ),
    ]