# Generated by Django 3.0.8 on 2020-07-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Day of the event', verbose_name='Event day')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('notes', models.TextField(blank=True, max_length=256, null=True)),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Practice')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]
