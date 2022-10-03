# Generated by Django 4.1 on 2022-09-27 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0017_remove_comment_post_xor_replied_to_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="postapp.post",
            ),
        ),
    ]