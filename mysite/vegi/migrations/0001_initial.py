# Generated by Django 4.2.5 on 2023-09-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recepie_name', models.CharField(max_length=100)),
                ('pecepie_desc', models.TextField()),
            ],
        ),
    ]