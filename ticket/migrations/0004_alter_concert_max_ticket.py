# Generated by Django 5.1 on 2024-08-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_concert_max_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='max_ticket',
            field=models.IntegerField(),
        ),
    ]
