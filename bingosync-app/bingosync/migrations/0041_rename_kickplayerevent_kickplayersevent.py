# Generated by Django 4.1.5 on 2023-07-06 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bingosync', '0040_remove_kickplayerevent_player_to_kick'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KickPlayerEvent',
            new_name='KickPlayersEvent',
        ),
    ]
