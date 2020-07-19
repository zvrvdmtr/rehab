# Generated by Django 3.0.8 on 2020-07-19 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Prcatice title')),
                ('descrioption', models.TextField(max_length=256, verbose_name='Practice description')),
                ('reps', models.PositiveIntegerField(verbose_name='Reps number')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
            options={
                'verbose_name': 'Practice',
                'verbose_name_plural': 'Practices',
            },
        ),
    ]
