# Generated by Django 4.1 on 2022-09-23 11:57

from django.db import migrations, models
import postapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0010_post_likes_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes_count",
            field=models.IntegerField(default=0),
        ),
    ]