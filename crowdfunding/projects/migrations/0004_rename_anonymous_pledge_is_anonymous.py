# Generated by Django 4.2.3 on 2024-01-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_pledge_supporter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='anonymous',
            new_name='is_anonymous',
        ),
    ]