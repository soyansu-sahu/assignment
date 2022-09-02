# Generated by Django 4.1 on 2022-09-02 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_no', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('profile_number', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]