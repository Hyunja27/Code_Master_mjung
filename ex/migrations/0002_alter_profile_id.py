# Generated by Django 3.2.4 on 2021-06-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
