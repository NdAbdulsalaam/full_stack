# Generated by Django 4.2.5 on 2023-09-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0002_category_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=225),
        ),
    ]