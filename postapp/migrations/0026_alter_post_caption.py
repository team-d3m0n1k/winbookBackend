# Generated by Django 4.1 on 2022-10-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0025_alter_post_caption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.TextField(default=""),
        ),
    ]
