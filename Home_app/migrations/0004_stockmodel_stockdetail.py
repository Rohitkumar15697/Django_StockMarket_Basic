# Generated by Django 3.1.5 on 2021-06-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0003_auto_20210622_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='stockdetail',
            field=models.TextField(null=True),
        ),
    ]
