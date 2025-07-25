# Generated by Django 5.2.3 on 2025-07-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('confirm_password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
                ('priority', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
