# Generated by Django 3.2.9 on 2021-11-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TWEET',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('time_crate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
