# Generated by Django 3.0.5 on 2020-06-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_auto_20200626_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='full_nmae',
            new_name='full_name',
        ),
    ]
