# Generated by Django 4.2.6 on 2023-10-28 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailling', '0002_alter_client_owner_alter_mailling_stop_to_send'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='mailling',
            old_name='status',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='mailling',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='owner',
            new_name='user',
        ),
    ]