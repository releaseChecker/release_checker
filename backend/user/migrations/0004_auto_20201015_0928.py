# Generated by Django 3.1.2 on 2020-10-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201014_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]