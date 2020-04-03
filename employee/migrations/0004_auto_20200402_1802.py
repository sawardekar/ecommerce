# Generated by Django 2.2.11 on 2020-04-02 12:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20200402_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='production_user',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='employee.Product'),
        ),
    ]