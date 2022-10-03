# Generated by Django 4.1 on 2022-10-03 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("postapp", "0019_alter_post_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_id",
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]