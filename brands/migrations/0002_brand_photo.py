# Generated by Django 4.1.1 on 2022-09-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
