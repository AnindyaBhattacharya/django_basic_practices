# Generated by Django 3.0.4 on 2020-04-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='PostingDate',
            field=models.DateField(db_column='Posting Date'),
        ),
    ]
