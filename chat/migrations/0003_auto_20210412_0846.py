# Generated by Django 3.1.7 on 2021-04-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210412_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='seen_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]