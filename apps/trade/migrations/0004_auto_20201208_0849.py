# Generated by Django 2.0.2 on 2020-12-08 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20201208_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='signer_mobile',
            new_name='singer_mobile',
        ),
    ]
