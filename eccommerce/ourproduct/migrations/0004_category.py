# Generated by Django 4.1.2 on 2023-04-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourproduct', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]