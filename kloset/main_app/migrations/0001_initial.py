# Generated by Django 4.0.6 on 2022-08-04 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.PositiveIntegerField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.PositiveIntegerField(max_length=10)),
                ('wallet', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
