# Generated by Django 3.0.4 on 2020-04-25 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_task_user_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task_user',
            old_name='id',
            new_name='ID',
        ),
    ]