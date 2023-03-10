# Generated by Django 4.1.5 on 2023-01-16 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_jobber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.IntegerField()),
                ('medicine', models.IntegerField()),
                ('third_party', models.IntegerField()),
                ('lost', models.BooleanField()),
                ('insuranceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insuranceId', to='first_jobber.insurance')),
            ],
        ),
    ]
