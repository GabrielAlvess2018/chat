# Generated by Django 2.0.7 on 2018-10-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
