# Generated by Django 4.1 on 2022-10-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0024_remove_post_url_or_caption_post_url_or_caption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]