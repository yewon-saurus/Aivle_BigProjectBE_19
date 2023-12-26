# Generated by Django 5.0 on 2023-12-26 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_introduction'),
        ('rank', '0005_alter_ranking_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_level',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank.ranking'),
        ),
    ]
