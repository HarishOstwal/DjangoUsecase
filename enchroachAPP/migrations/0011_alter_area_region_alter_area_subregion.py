# Generated by Django 4.2.5 on 2023-09-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enchroachAPP', '0010_remove_encroachment_area_area_id_alter_area_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='region',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='area',
            name='subregion',
            field=models.CharField(max_length=255),
        ),
    ]
