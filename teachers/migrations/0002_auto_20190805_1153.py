# Generated by Django 2.2 on 2019-08-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createteacher',
            name='photo',
            field=models.ImageField(upload_to='media/teacher'),
        ),
    ]
