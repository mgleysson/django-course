# Generated by Django 3.1.1 on 2020-10-02 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201002_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('-title',)},
        ),
    ]
