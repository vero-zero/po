# Generated by Django 4.2 on 2023-04-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Items_List",
            fields=[
                ("name", models.TextField(primary_key=True, serialize=False)),
                ("imgs", models.TextField()),
            ],
            options={
                "db_table": "Items_List",
                "managed": False,
            },
        ),
    ]
