# Generated by Django 3.0.4 on 2020-04-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelFormsApp', '0002_auto_20200426_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedb',
            name='points',
            field=models.IntegerField(db_column='Rating', default=0),
        ),
    ]