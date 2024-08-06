# Generated by Django 5.0.7 on 2024-07-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('zip', models.CharField(blank=True, max_length=255)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group', models.IntegerField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
            ],
        ),
    ]