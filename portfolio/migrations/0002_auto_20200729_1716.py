# Generated by Django 3.0.8 on 2020-07-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coca',
            name='discription',
            field=models.TextField(max_length=9000),
        ),
    ]
