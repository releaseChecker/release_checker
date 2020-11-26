# Generated by Django 3.1.2 on 2020-10-28 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_history'),
        ('user', '0005_auto_20201015_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='library.library'),
        ),
    ]
