# Generated by Django 5.1 on 2024-09-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_concert_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='max_ticket',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
