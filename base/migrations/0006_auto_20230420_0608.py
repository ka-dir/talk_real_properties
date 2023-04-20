# Generated by Django 3.2.12 on 2023-04-20 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20230417_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertytype',
            name='property',
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.propertytype'),
        ),
    ]
