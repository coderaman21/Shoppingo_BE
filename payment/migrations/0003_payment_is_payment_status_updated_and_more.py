# Generated by Django 4.2.4 on 2023-09-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="is_payment_status_updated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_detail",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="payment",
            name="razorpay_signature",
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="payment",
            name="order_id",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("created", "Created"),
                    ("authorised", "Authorised"),
                    ("captured", "Captured"),
                    ("failed", "Failed"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="razorpay_order_id",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="payment",
            name="razorpay_payment_id",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
    ]
