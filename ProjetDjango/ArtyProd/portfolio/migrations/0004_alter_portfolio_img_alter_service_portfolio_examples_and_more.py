# Generated by Django 4.1.7 on 2023-05-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_contact_teammember_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='Img',
            field=models.ImageField(blank=True, upload_to='static/assets/img/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='portfolio_examples',
            field=models.ManyToManyField(related_name='portfolio_examples', to='portfolio.portfolio'),
        ),
        migrations.DeleteModel(
            name='PortfolioImage',
        ),
    ]
