# Generated by Django 3.1.1 on 2020-12-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(verbose_name='Date creatio')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
            ],
        ),
    ]
