# Generated by Django 3.2.12 on 2023-04-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_propertytype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertytype',
            name='category',
            field=models.CharField(blank=True, choices=[('Land', 'Land'), ('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Industrial', 'Industrial')], max_length=100, null=True),
        ),
    ]
