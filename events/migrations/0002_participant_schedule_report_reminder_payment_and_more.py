# Generated by Django 4.2.2 on 2023-07-02 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Participants', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.DateTimeField()),
                ('session_duration', models.DurationField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='events.event')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.PositiveIntegerField()),
                ('session_popularity', models.PositiveIntegerField()),
                ('speaker_ratings', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_time', models.DateTimeField()),
                ('Participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='events.participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.participant')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='sessions',
            field=models.ManyToManyField(to='events.schedule'),
        ),
    ]
