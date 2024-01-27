# Generated by Django 4.2.5 on 2024-01-04 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('departments', models.CharField(choices=[('gynocology', 'GYNOCOLOGY'), ('cardiology', 'CARDIOLOGY'), ('ent', 'ENT'), ('neurology', 'NEUROLOGY'), ('orthopedic', 'ORTHOPEDIC')], max_length=20)),
            ],
        ),
    ]