# Generated by Django 3.1.4 on 2021-04-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='key',
            field=models.CharField(blank=True, default='97e796', editable=False, max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.TextField(unique=True),
        ),
    ]
