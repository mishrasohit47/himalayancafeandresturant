# Generated by Django 4.1.2 on 2023-03-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourproduct', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ordered_at',
            new_name='prepared_at',
        ),
    ]
