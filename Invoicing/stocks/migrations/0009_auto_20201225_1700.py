# Generated by Django 2.2 on 2020-12-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_auto_20201225_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articleType',
            field=models.CharField(choices=[('srv', 'service'), ('prod', 'product')], max_length=100),
        ),
    ]