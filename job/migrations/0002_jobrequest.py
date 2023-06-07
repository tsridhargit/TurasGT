# Generated by Django 3.2 on 2021-11-22 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
        ('accounts', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('seen_status', models.PositiveSmallIntegerField(choices=[(1, 'seen'), (0, 'not seen')], default=0, verbose_name='seen status')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'waiting'), (1, 'denied')], default=0, verbose_name='status')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_requests', to='job.job', verbose_name='job')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_requests', to='accounts.jobseeker', verbose_name='job seeker')),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_requests', to='resume.resume', verbose_name='resume')),
            ],
            options={
                'verbose_name': 'job request',
                'verbose_name_plural': 'job requests',
                'db_table': 'job_request',
            },
        ),
    ]
