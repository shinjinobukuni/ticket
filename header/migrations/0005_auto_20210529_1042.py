# Generated by Django 2.2.2 on 2021-05-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0004_auto_20210529_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='limit_date',
            field=models.DateField(blank=True, null=True, verbose_name='期限'),
        ),
    ]