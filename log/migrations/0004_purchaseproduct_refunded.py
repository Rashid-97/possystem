# Generated by Django 4.1.5 on 2023-06-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_rename_purchaseproductrefundlog_purchaseproductrefund_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseproduct',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
    ]