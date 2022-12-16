# Generated by Django 2.2 on 2019-07-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('office', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
    ]
