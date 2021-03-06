# Generated by Django 3.2.7 on 2021-10-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0016_auto_20211012_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='light',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='media',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preset',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video_wall',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
