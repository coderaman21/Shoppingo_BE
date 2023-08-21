# Generated by Django 4.2.4 on 2023-08-21 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("order_date", models.DateTimeField()),
                ("order_lifecycle", models.JSONField(default=dict)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("booked", "Booked"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("cancelled", "Cancelled"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "order_id",
                    models.CharField(blank=True, db_index=True, max_length=50),
                ),
                ("order_location", models.TextField(blank=True)),
                ("total_item", models.IntegerField(default=1)),
                ("paid_amount", models.CharField(max_length=50)),
                ("expected_delivery", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.product"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]