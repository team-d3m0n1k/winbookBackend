# Generated by Django 4.1 on 2022-10-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0033_remove_post_url_or_caption_post_url_or_caption"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="post",
            name="url_or_caption",
        ),
        migrations.AddConstraint(
            model_name="post",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("caption__exact", ""), ("url__exact", ""), _negated=True
                ),
                name="url_or_caption",
                violation_error_message="Post must have atleast a url or a caption",
            ),
        ),
    ]
