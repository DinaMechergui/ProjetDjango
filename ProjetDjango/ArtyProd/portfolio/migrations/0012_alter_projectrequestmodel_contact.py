# Generated by Django 4.1.7 on 2023-05-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_projectrequestmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequestmodel',
            name='contact',
            field=models.TextField(blank=True),
        ),
    ]
