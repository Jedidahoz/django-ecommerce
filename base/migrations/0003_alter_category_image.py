# Generated by Django 5.0 on 2024-02-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_category_options_alter_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='vendor.jpg', upload_to='category'),
        ),
    ]
