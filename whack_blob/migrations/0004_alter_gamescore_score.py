# Generated by Django 4.2 on 2023-04-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whack_blob', '0003_alter_gamescore_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]