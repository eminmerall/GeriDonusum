# Generated by Django 3.0.5 on 2020-05-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='firma',
            fields=[
                ('fId', models.AutoField(primary_key=True, serialize=False)),
                ('fAdi', models.TextField(db_column='Adı', max_length=200, verbose_name='Adı')),
                ('fTel', models.TextField(db_column='Telefon', max_length=20, verbose_name='Telefon')),
                ('fAdres', models.TextField(db_column='Adres', max_length=400, verbose_name='Adres')),
                ('feMail', models.EmailField(db_column='Email', max_length=254, verbose_name='E-Mail')),
            ],
        ),
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('kId', models.AutoField(primary_key=True, serialize=False)),
                ('kAdi', models.TextField(db_column='Adı', max_length=100, verbose_name='Adı')),
                ('kSoyadi', models.TextField(db_column='Soyadı', max_length=100, verbose_name='Soyadı')),
                ('kTel', models.TextField(db_column='Telefon', max_length=20, verbose_name='Telefon')),
                ('kAdres', models.TextField(db_column='Adres', max_length=400, verbose_name='Adres')),
                ('keMail', models.EmailField(db_column='Email', max_length=254, verbose_name='E-Mail')),
            ],
        ),
    ]
