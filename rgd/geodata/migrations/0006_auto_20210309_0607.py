# Generated by Django 3.2a1 on 2021-03-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0005_auto_20210308_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandmetaentry',
            name='max',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bandmetaentry',
            name='mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bandmetaentry',
            name='min',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bandmetaentry',
            name='std',
            field=models.FloatField(null=True),
        ),
    ]