# Generated by Django 4.2.6 on 2023-10-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]