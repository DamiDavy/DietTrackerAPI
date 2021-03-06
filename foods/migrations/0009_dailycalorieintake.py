# Generated by Django 3.2.7 on 2021-09-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_alter_fooditem_date_for_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCalorieIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('daily_calorie_intake', models.IntegerField()),
            ],
        ),
    ]
