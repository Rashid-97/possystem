# Generated by Django 4.1.5 on 2023-02-19 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Alan işçi'),
        ),
        migrations.AlterField(
            model_name='purchaseproductrefundlog',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Geri qaytarılma tarixi'),
        ),
        migrations.AlterField(
            model_name='purchaseproductrefundlog',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Geri qaytaran işçi'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Satış aparan işçi'),
        ),
    ]