# Generated by Django 2.1.3 on 2018-11-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('repo', models.CharField(max_length=120)),
            ],
        ),
    ]
