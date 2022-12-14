# Generated by Django 4.1 on 2022-10-25 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("katalog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pesan",
            name="toko",
        ),
        migrations.RemoveField(
            model_name="pesan",
            name="user",
        ),
        migrations.CreateModel(
            name="Channel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "toko",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="katalog.toko"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pesan",
            name="channel",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="chat.channel",
            ),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name="channel",
            index=models.Index(fields=["toko", "user"], name="toko_user_idx"),
        ),
        migrations.AddConstraint(
            model_name="channel",
            constraint=models.UniqueConstraint(
                fields=("toko", "user"), name="toko_user_uq"
            ),
        ),
    ]
