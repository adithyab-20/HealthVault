# Generated by Django 3.1.7 on 2021-05-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='columbiaasia_doctor',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]