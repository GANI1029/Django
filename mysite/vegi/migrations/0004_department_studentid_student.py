# Generated by Django 4.2.5 on 2023-10-09 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegi', '0003_receipes_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='StudentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_age', models.IntegerField(default=18)),
                ('student_address', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='vegi.department')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='vegi.studentid')),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['student_name'],
            },
        ),
    ]