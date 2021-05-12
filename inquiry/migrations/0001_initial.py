# Generated by Django 3.1.7 on 2021-04-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_course_master_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='inquiry_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry_date', models.DateField()),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('st_name', models.CharField(max_length=30)),
                ('area_name', models.CharField(max_length=30)),
                ('city_name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=11)),
                ('phone_number_house', models.CharField(max_length=11)),
                ('education', models.CharField(max_length=30)),
                ('college_name', models.CharField(max_length=50)),
                ('referance_name', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=20)),
                ('inquiry_held_by', models.CharField(max_length=30)),
                ('inquiry_institute_phone', models.CharField(max_length=11)),
                ('demo_lecture_date', models.DateField()),
                ('demo_lecture_time', models.TimeField()),
                ('course', models.ManyToManyField(related_name='inquiry', to='course.course_master')),
            ],
        ),
    ]