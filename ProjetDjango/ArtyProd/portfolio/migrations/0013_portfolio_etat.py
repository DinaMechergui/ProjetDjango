# Generated by Django 4.1.7 on 2023-05-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_projectrequestmodel_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='etat',
            field=models.CharField(choices=[('acheve', 'acheve'), ('en cours', 'en cours'), ('request', 'request')], default='request', max_length=50),
        ),
    ]