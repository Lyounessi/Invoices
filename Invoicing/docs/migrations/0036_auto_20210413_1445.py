# Generated by Django 2.2 on 2021-04-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0035_auto_20210408_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='tax_one',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='tax_two',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='total',
        ),
        migrations.AddField(
            model_name='article_inv',
            name='inv_tax_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='article_inv',
            name='inv_tax_two',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='article_inv',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='article_inv',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]
