# Generated by Django 4.1 on 2022-10-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0030_remove_post_url_or_caption_post_url_or_caption"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="post",
            name="url_or_caption",
        ),
    ]
