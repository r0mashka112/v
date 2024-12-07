# Generated by Django 4.2.16 on 2024-11-25 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormOfEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'form-education',
                'verbose_name_plural': 'form-educations',
                'db_table': 'form-education',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'speciality',
                'verbose_name_plural': 'specialities',
                'db_table': 'specialities',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('year_of_entry', models.IntegerField()),
                ('year_of_ending', models.IntegerField()),
                ('form_of_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.formofeducation')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.group')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'db_table': 'students',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.speciality'),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number_of_hours', models.IntegerField()),
                ('reporting_form', models.CharField(max_length=50)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.speciality')),
            ],
            options={
                'verbose_name': 'discipline',
                'verbose_name_plural': 'disciplines',
                'db_table': 'disciplines',
            },
        ),
        migrations.CreateModel(
            name='AcademicPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('mark', models.IntegerField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.discipline')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'verbose_name': 'academic_performance',
                'verbose_name_plural': 'academic_performances',
                'db_table': 'academic_performance',
            },
        ),
    ]