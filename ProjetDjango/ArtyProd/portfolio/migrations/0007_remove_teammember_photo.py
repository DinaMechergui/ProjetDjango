# Generated by Django 4.1.7 on 2023-05-06 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_desprojets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='photo',
        ),
    ]
