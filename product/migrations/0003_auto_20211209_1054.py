# Generated by Django 3.2.9 on 2021-12-09 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211207_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(),
        ),
    ]
