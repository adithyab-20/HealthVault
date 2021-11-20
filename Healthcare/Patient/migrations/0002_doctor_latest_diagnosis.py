# Generated by Django 3.1.7 on 2021-06-07 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_latest_diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('diagnosis', models.TextField()),
                ('diagnosis_description', models.TextField()),
                ('doctor_advice', models.TextField()),
                ('additional_comments', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lastest_diagnosis_doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='latest_diagnois_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]