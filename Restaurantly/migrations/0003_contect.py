# Generated by Django 4.2 on 2024-07-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantly', '0002_alter_bookatable_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=255)),
            ],
        ),
    ]
