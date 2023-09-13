# Generated by Django 4.2.5 on 2023-09-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('manager', 'manager'), ('officer', 'officer'), ('cashier', 'cashier'), ('user', 'user')], default='user', max_length=10),
        ),
    ]
