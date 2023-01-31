# Generated by Django 4.1.5 on 2023-01-31 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_belongs_to_user_is_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='belongs_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
    ]
