# Generated by Django 3.0.4 on 2020-04-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=50)),
                ('L_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
