# Generated by Django 4.1.2 on 2023-05-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourproduct', '0009_alter_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
