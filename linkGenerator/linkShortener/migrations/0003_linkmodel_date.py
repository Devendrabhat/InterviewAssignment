# Generated by Django 2.0.3 on 2018-03-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkShortener', '0002_auto_20180324_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
