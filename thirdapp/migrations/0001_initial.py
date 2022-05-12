# Generated by Django 3.2.5 on 2022-05-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=100, null=True)),
                ('shop_desc', models.CharField(max_length=100, null=True)),
                ('rest_date', models.CharField(max_length=100, null=True)),
                ('parking_info', models.CharField(max_length=100, null=True)),
                ('img_path', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'shop',
                'managed': False,
            },
        ),
    ]