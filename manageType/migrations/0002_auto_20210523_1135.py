# Generated by Django 2.2.2 on 2021-05-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageType', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='名前'),
        ),
    ]
