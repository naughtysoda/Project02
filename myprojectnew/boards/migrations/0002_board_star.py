# Generated by Django 3.1.4 on 2021-01-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='star',
            field=models.IntegerField(default=0, null=True),
        ),
    ]