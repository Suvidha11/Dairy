# Generated by Django 4.1.3 on 2023-05-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_memo_is_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memo',
            name='is_private',
        ),
        migrations.AddField(
            model_name='memo',
            name='Privcy',
            field=models.CharField(default='Public', max_length=10),
        ),
    ]