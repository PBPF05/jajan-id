# Generated by Django 4.1 on 2022-10-16 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
        ("katalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pesan",
            name="toko",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="katalog.toko"
            ),
        ),
        migrations.AddField(
            model_name="pesan",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]