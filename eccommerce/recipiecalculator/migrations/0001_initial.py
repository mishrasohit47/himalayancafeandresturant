# Generated by Django 4.1.2 on 2023-05-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('direction', models.CharField(max_length=250)),
                ('date_posted', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
