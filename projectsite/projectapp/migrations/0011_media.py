# Generated by Django 3.2.7 on 2021-10-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0010_remove_light_hexcolour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('media_name', models.CharField(max_length=255, null=True)),
                ('file_path', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
