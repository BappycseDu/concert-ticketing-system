# Generated by Django 5.1 on 2024-09-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]