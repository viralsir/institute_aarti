# Generated by Django 3.1.7 on 2021-04-08 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_course_master_fees'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmission_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_addmission', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('scan_copy_of_id_proof', models.FileField(upload_to='documents')),
                ('fees', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive'), ('Close', 'Close')], max_length=10)),
                ('no_of_days', models.IntegerField()),
                ('remarks', models.CharField(max_length=20)),
                ('pending_fees', models.IntegerField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='addmissions', to='course.course_master')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addmissions', to='student.student_personal_info')),
            ],
        ),
    ]
