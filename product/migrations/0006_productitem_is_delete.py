# Generated by Django 3.2.9 on 2021-12-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
