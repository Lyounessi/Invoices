# Generated by Django 3.2 on 2021-04-20 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actif', models.BooleanField(default=True, null=True)),
                ('number', models.CharField(max_length=50, null=True)),
                ('companyName', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=50)),
                ('countrie', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('postCode', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('taxNum', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('website', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True, max_length=50, null=True)),
                ('payments_conditions', models.CharField(choices=[('30', '30 days'), ('END', 'End of the current month')], max_length=10, null=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
