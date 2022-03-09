# Generated by Django 3.2.12 on 2022-03-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0005_mentor_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='bio',
            field=models.TextField(default="I'm a really good developer"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='title',
            field=models.CharField(default="Developer", max_length=50),
            preserve_default=False,
        ),
    ]
