# Generated by Django 3.2.9 on 2021-12-05 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0007_auto_20211129_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_id', models.IntegerField(default=1, unique=True)),
                ('ability_name', models.CharField(default='', max_length=100)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
    ]
