# Generated by Django 5.0.3 on 2024-03-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_recipe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
