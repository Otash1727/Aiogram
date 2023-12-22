# Generated by Django 4.0.8 on 2023-12-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_users_active_courses_alter_users_cashback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='logo_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='information.courses'),
        ),
    ]