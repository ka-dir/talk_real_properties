# Generated by Django 3.2.12 on 2023-04-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
