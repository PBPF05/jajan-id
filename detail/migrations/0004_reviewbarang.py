# Generated by Django 4.1 on 2022-11-02 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_barang_nama'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=128)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.barang')),
            ],
        ),
    ]
