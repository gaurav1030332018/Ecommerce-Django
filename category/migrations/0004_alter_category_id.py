# Generated by Django 4.1.2 on 2022-11-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20221102_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
