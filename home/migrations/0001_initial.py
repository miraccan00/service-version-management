# Generated by Django 3.2.6 on 2023-05-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseProject1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('release_artifact', models.CharField(max_length=100)),
                ('release_number', models.CharField(max_length=50)),
                ('release_path', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('microui', models.BooleanField()),
                ('sql', models.BooleanField()),
                ('uat', models.BooleanField()),
                ('prod', models.BooleanField()),
            ],
        ),
    ]
