# Generated by Django 5.1 on 2024-09-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_alter_concert_max_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='concert',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
        migrations.AddField(
            model_name='ticket',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash')], default='credit_card', max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(blank=True, max_length=6, unique=True),
        ),
    ]
