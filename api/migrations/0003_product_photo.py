# Generated by Django 5.0.6 on 2024-05-31 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_alter_employee_managers_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='api/images'),
        ),
    ]
