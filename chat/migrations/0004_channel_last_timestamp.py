# Generated by Django 4.1 on 2022-10-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_remove_pesan_toko_remove_pesan_user_channel_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="last_timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
