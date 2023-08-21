# Generated by Django 4.2.4 on 2023-08-21 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("home", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="usercart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.category"
            ),
        ),
        migrations.AddField(
            model_name="productreview",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_review",
                to="home.product",
            ),
        ),
        migrations.AddField(
            model_name="productreview",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_product_review",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.brand"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.subcategory",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(to="home.producttag"),
        ),
        migrations.AddField(
            model_name="inventory",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.product"
            ),
        ),
    ]