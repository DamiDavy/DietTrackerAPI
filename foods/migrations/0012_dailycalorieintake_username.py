# Generated by Django 3.2.7 on 2021-10-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20211009_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailycalorieintake',
            name='username',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
