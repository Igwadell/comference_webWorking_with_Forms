# Generated by Django 2.2.28 on 2023-07-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
