# Generated by Django 3.1.6 on 2021-02-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210218_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='image',
            field=models.FilePathField(),
        ),
    ]