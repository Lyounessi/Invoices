# Generated by Django 3.2 on 2021-04-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_invoices_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
        ),
    ]
