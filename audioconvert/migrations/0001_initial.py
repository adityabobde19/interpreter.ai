# Generated by Django 4.0.6 on 2022-08-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('ilang', models.CharField(default='English', max_length=1000000)),
                ('tlang', models.CharField(default='English', max_length=1000000)),
            ],
        ),
    ]
