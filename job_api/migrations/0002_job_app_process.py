# Generated by Django 4.0.3 on 2022-04-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='app_process',
            field=models.CharField(choices=[('interested', 'Interested'), ('applied', 'Applied'), ('interviewing', 'Interviewing'), ('offer', 'Offer'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='interested', max_length=30),
        ),
    ]