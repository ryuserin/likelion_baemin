# Generated by Django 3.2.6 on 2021-08-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baeminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=100)),
                ('pay', models.CharField(choices=[('배민', '배민페이'), ('신용', '신용카드'), ('계좌', '계좌이체'), ('무통장', '무통장입금')], max_length=200)),
            ],
        ),
    ]