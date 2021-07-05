# Generated by Django 3.2.4 on 2021-06-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='stockmodel',
            unique_together={('stockname', 'slug')},
        ),
    ]