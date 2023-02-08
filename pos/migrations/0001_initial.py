# Generated by Django 4.1.5 on 2023-02-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_remove_shop_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Əlaqə nömrəsi')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shop', verbose_name='Mağaza')),
            ],
        ),
    ]