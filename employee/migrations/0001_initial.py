# Generated by Django 2.2.11 on 2020-04-02 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('mobile', models.BigIntegerField(blank=True, max_length=12, null=True, unique=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.EmployeeType')),
            ],
        ),
    ]