# Generated by Django 4.0.8 on 2023-12-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='active_courses',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='cashback',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='debt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='extra_role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='invite_people',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='payments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]