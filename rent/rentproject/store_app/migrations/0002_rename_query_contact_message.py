# Generated by Django 4.2.5 on 2023-09-24 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='query',
            new_name='message',
        ),
    ]
