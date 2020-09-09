# Generated by Django 3.0.4 on 2020-08-20 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=False),
        ),
    ]
