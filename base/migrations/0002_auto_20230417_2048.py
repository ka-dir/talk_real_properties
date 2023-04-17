# Generated by Django 3.2.12 on 2023-04-17 20:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.OneToOneField(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.propertytype'),
        ),
    ]
