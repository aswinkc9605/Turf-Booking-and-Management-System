# Generated by Django 3.2.20 on 2024-01-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=8)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
    ]
