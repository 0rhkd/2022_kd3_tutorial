# Generated by Django 3.2.5 on 2022-05-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_rename_name_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armyshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('type', models.TextField()),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'army_shop',
                'managed': False,
            },
        ),
    ]