# Generated by Django 4.1.7 on 2023-02-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_category_product_date_added_product_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_type',
            field=models.CharField(blank=True, choices=[('KG', 'KG'), ('Gram', 'Gram'), ('Ton', 'Ton'), ('Piece', 'Piece')], max_length=60, null=True),
        ),
    ]
